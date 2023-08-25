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
    for i in range(1, Runs + 1):
        print("Run:", i)
        tag = "1_1"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "1_2"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "1_3"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "1_5"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "1_10"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 10
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 11
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)
        ################################## 2 Cubic flows#############################
        tag = "2_1"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "2_2"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "2_3"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "2_5"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "2_10"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 10
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 11
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 12
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        ################################## 3 Cubic flows#############################
        tag = "3_1"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "3_2"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "3_3"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "3_5"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "3_10"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 10
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 11
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 12
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 13
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

    ################################## 4 Cubic flows#############################
        tag = "4_1"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "4_2"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "4_3"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "4_5"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "4_10"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 10
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 11
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 12
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 13
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 14
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

    ################################## 5 Cubic flows#############################
        tag = "5_1"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "5_2"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "5_3"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "5_5"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 10
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "5_10"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 10
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 11
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 12
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 13
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 14
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 15
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

    ################################## 6 Cubic flows#############################
        tag = "6_1"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "6_2"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "6_3"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "6_5"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 10
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 11
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "6_10"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 10
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 11
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 12
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 13
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 14
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 15
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 16
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

    ################################## 7 Cubic flows#############################
        tag = "7_1"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "7_2"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "7_3"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 10
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "7_5"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 10
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 11
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 12
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "7_10"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 10
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 11
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 12
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 13
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 14
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 15
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 16
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 17
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

    ################################## 8 Cubic flows#############################
        tag = "8_1"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "8_2"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 10
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "8_3"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 10
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 11
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "8_5"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 10
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 11
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 12
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 13
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "8_10"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 10
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 11
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 12
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 13
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 14
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 15
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 16
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 17
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 18
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

    ################################## 9 Cubic flows#############################
        tag = "9_1"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 10
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "9_2"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 10
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 11
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "9_3"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 10
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 11
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 12
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "9_5"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 10
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 11
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 12
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 13
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 14
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "9_10"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 10
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 11
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 12
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 13
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 14
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 15
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 16
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 17
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 18
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 19
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

    ################################## 10 Cubic flows#############################
        tag = "10_1"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 10
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 11
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "10_2"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 10
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 11
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 12
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "10_3"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 10
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 11
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 12
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 13
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "10_5"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 10
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 11
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 12
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 13
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 14
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 15
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

        tag = "10_10"    
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 3
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 4
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 5
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 6
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 7
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 8
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 9
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 10
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", tag, i)
        flow = 11
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 12
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 13
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 14
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 15
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 16
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 17
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 18
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 19
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)
        flow = 20
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", tag, i)

        time.sleep(duration + 3)

    sys.stdout.write("\rTest is done\n")

if __name__ == '__main__':
    main()

    
    