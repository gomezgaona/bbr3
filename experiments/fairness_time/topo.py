#!/usr/bin/python

import os
import subprocess
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch
from mininet.cli import CLI

def start_mininet_hosts(num_hosts, buffer_size, btlbw, delay):
    if(num_hosts > 254):
        print("You are trying to add more than 254 senders and receivers")
        return
    net = Mininet(topo=None, build=False, ipBase='10.0.0.0/16')

    # Create switches
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch, failMode='standalone')
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch, failMode='standalone')
    print("Creating switches")

    # Connect s1<->s2
    net.addLink(s1, s2)
    print("Connecting switch s1 to switch s2")

    num_hosts = int(num_hosts/2)
    
    # Start hosts and connect them to the switch
    for i in range(1, num_hosts + 1):
        # Senders (hs)
        hs = net.addHost(f'hs{i}', ip=f'10.0.0.{i}/16')
        hs.cmd('sysctl -w net.ipv4.tcp_wmem="{} {} {}"'.format(buffer_size, buffer_size, buffer_size))
        hs.cmd('sysctl -w net.ipv4.tcp_rmem="{} {} {}"'.format(buffer_size, buffer_size, buffer_size))
        net.addLink(hs, s1)
        # Receivers (hr)
        hr = net.addHost(f'hr{i}', ip=f'10.0.1.{i}/16')
        hr.cmd('sysctl -w net.ipv4.tcp_wmem="{} {} {}"'.format(buffer_size, buffer_size, buffer_size))
        hr.cmd('sysctl -w net.ipv4.tcp_rmem="{} {} {}"'.format(buffer_size, buffer_size, buffer_size))
        net.addLink(hr, s2)
        #print(i)
    print(f"Creating hosts, setting TCP send and receive buffers to {buffer_size}, and connecting hosts to the switches")

    # Start the network
    net.start()
    print("Starting the network")

    # Setting the Delay and Limiting the Bottleneck Bandwidth
    burst = int(btlbw/250/8)
    limit = int(btlbw*delay*(1.024**2)/8) # Setting the limit to BDP
    print(limit)

    
    netem_cmd_s1 = f'tc qdisc add dev s1-eth1 root handle 1: netem delay {delay}s'
    tbf_cmd = f'tc qdisc add dev s1-eth1 parent 1: handle 2: tbf rate {btlbw} burst {burst} limit {limit}'
    
    netem_cmd_s2 = f'tc qdisc add dev s2-eth1 root handle 1: netem delay {delay}s'

    os.system(netem_cmd_s1)
    #os.system(netem_cmd_s2)
    print(f"Setting the delay to {2*delay} seconds")

    os.system(tbf_cmd)
    print(f"Limiting the bottleneck bandwidth to {btlbw} bps")
   

    # Starting iperf3 servers
    for i in range(1, num_hosts + 1):
         hr = net[f'hr{i}']
         hr.cmd('iperf3 -s &> /dev/null&')
    print("Starting iperf3 server on the receivers (hr)")

    # Open the Mininet CLI
    net.interact()
    
    # Clean up after the network has been stopped
    net.stop()

# Enter the number of hosts
num_hosts = 12
TCP_buffer_size = "4096 1000000 200000000"
btlbw = int(1e9)
delay = 20e-3/2

start_mininet_hosts(num_hosts, TCP_buffer_size, btlbw, delay)
