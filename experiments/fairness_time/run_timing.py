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

def run_iperf_test(host, flow, dst_IP, duration, cc, run):
    cmd = f'{host} iperf3 -c {dst_IP} -t {duration}  -C {cc} -J > json_files/h{flow}_{cc}_out_{run}.json &'
    os.system(cmd)

def change_BDP(BDP):
    btlbw = 1e9
    delay = 2e-3
    burst = int(btlbw/250/8)
    limit = int(BDP*btlbw*delay*(1.024**2)/8) # Setting the limit to BDP

    sys.stdout.write(f"\n\rCurrent BDP: {BDP}\n" )
    tbf_cmd = f'tc qdisc change dev s1-eth1 root handle 1: tbf rate {btlbw} burst {burst} limit {limit}'
    os.system(tbf_cmd)

def main():
    h = '/home/admin/mininet/util/m hs'
    Runs = 10
    for run in range(1, Runs + 1):
        duration = 480
        print("Flow 1: CUBIC started")
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", run)
        time.sleep(60)

        print("Flow 2: BBRv3 started\n")
        flow = 2
        duration -= 60
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", run)
        time.sleep(60)

        print("Flow 3: BBRv3 started\n")
        flow = 3
        duration -= 60
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", run)
        time.sleep(60)

        print("Flow 4: BBRv3 started\n")
        flow = 4
        duration -= 60
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", run)
        time.sleep(60)

        print("Flow 5: BBRv3 started\n")
        flow = 5
        duration -= 60
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", run)
        time.sleep(60)

        print("Flow 6: BBRv3 started\n")
        flow = 6
        duration -= 60
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", run)
        time.sleep(200)

    sys.stdout.write("\n\rTest is done\n")
    time.sleep(5)

if __name__ == '__main__':
    main()

    
    