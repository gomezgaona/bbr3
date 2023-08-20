import json
import os

from mininet.net import Mininet
from mininet.node import Host
from mininet.link import TCLink
from mininet.topo import Topo
import threading
import time
import sys

# Define the timer function
def timer_function(duration):
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        remaining_time = end_time - time.time()
        sys.stdout.write("\rTime remaining: {:.2f} seconds".format(remaining_time))
        sys.stdout.flush()
        time.sleep(1)  # Update every 1 second

    print("Timer has finished!")

def run_iperf_test(host, flow, dst_IP, duration, cc):
    cmd = f'{host} iperf3 -c {dst_IP} -t {duration}  -C {cc} -J > json_files/h{flow}_{cc}_out.json &'
    os.system(cmd)

def change_btlbw(btlbw):
    delay = 20e-3
    BDP = 1
    burst = int(btlbw/250/8)
    limit = int(BDP*btlbw*delay*(1.024**2)/8) # Setting the limit to BDP

    sys.stdout.write(f"\n\rCurrent BDP: {BDP}\n" )
    tbf_cmd = f'tc qdisc change dev s1-eth1 parent 1: handle 2: tbf rate {btlbw} burst {burst} limit {limit}'
    os.system(tbf_cmd)

def main():
    h = '/home/admin/mininet/util/m hs'
    
    duration = 300
    print("Starting test")

    print("Changing Btlbw to 500Mbps")
    change_btlbw(0.5e9)
    time.sleep(5)
    flow = 1
    run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr")
    time.sleep(60)

    print("Changing Btlbw to 1Gbps")
    change_btlbw(1e9)
    time.sleep(60)
    
    print("Changing Btlbw to 500Mbps")
    change_btlbw(0.5e9)
    time.sleep(60)
    
    print("Changing Btlbw to 1Gbps")
    change_btlbw(1e9)
    time.sleep(60)
    
    print("Changing Btlbw to 500Mbps")
    change_btlbw(0.5e9)
    time.sleep(60)
    
    sys.stdout.write("\n\rTest is done\n")
    time.sleep(5)

if __name__ == '__main__':
    main()

    
    