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

def run_iperf_test(host, flow, dst_IP, duration, cc, BDP, i):
    
    cmd = f'{host} iperf3 -c {dst_IP} -t {duration}  -C {cc} -J > json_files/h{flow}_{cc}_{BDP}BDP_out_{i}.json &'
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
    duration = 120 ##############Change this 120 ############
    BDP = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    Runs = 10
    N_flows = 100
    for i in range(1, Runs + 1):
        for bdp in BDP:
            change_BDP(bdp)
            for flow in range(1, N_flows + 1):
                if flow <= N_flows / 2 :
                    run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", bdp, i)
                else:
                    run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", bdp, i)
            time.sleep(duration + 10)
    '''
    for i in range(1, Runs + 1):
        for bdp in BDP:

            change_BDP(bdp)
        
            flow = 1
            run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", bdp, i)
            flow = 2
            run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", bdp, i)

            time.sleep(duration + 3)
    '''
    sys.stdout.write("\rTest is done\n")

if __name__ == '__main__':
    main()

    
    