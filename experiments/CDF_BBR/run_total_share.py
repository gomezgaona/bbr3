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

def run_iperf_test(host, flow, dst_IP, duration, cc, tag, i):
    
    cmd = f'{host} iperf3 -c {dst_IP} -t {duration}  -C {cc} -J > json_files/h{flow}_{cc}_{tag}_{i}.json &'
    os.system(cmd)

def change_BDP(BDP):
    btlbw = 1e9
    delay = 20e-3
    burst = int(btlbw/250/8)
    limit = int(BDP*btlbw*delay*(1.024**2)/8) # Setting the limit to BDP
    sys.stdout.write(f"\rCurrent BDP: {BDP}\n" )

    tbf_cmd = f'tc qdisc change dev s1-eth1 parent 1: handle 2: tbf rate {btlbw} burst {burst} limit {limit}'
    os.system(tbf_cmd)

def main():
    h = '/home/admin/mininet/util/m hs'
    duration = 120 
    
    Runs = 10
    #N_flows = 100
    
    change_BDP(1)
    
    print("Run:", i)
    tag = "1_1"    
    flow = 1
    run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
    flow = 2
    run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

    time.sleep(duration + 3)

       
    sys.stdout.write("\rTest is done\n")

if __name__ == '__main__':
    main()

    
    