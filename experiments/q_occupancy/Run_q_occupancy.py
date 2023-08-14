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

def change_BDP(BDP):
    btlbw = 1e9
    delay = 2e-3
    burst = int(btlbw/250/8)
    limit = int(BDP*btlbw*delay*(1.024**2)/8) # Setting the limit to BDP

    sys.stdout.write(f"\n\rCurrent BDP: {BDP}\n" )
    tbf_cmd = f'tc qdisc change dev s1-eth1 root handle 1: tbf rate {btlbw} burst {burst} limit {limit}'
    os.system(tbf_cmd)
'''
def change_delay(delay):
      
    sys.stdout.write(f"\rCurrent delay: {delay}\n" )
    netem_cmd_s1 = f'tc qdisc change dev s1-eth1 root handle 1: netem delay {delay/2}s loss 0.0046%'
    netem_cmd_s2 = f'tc qdisc change dev s2-eth1 root handle 1: netem delay {delay/2}s'
    #tbf_cmd = f'tc qdisc add dev s1-eth1 root tbf rate {btlbw} burst {burst} limit {limit}'
    os.system(netem_cmd_s1)
    os.system(netem_cmd_s2)
'''
def get_q_occupancy(cc):
     
     while True:
        os.system(f'tc -s qdisc show dev s1-eth1 | head -3 | tail -1| cut -d " " -f3 >> cubic_q_occupancy.dat')
        time.sleep(1)

def main():
    h = '/home/admin/mininet/util/m hs'
    duration = 480
    BDP = [0.5, 1, 10, 10, 1, 0.5]
    cc = "bbr"
    change_BDP(BDP[0])

    # Create a thread for the timer function
    timer_thread = threading.Thread(target=timer_function, args=(duration,))
    os.system("rm cubic_q_occupancy.dat")
    q_polling = threading.Thread(target=get_q_occupancy, args=(cc,))
    q_polling.start()

    flow = 1
    run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, cc)
    #os.system(f'while true; do sudo  tc -s qdisc show dev s1-eth1 | tail -2 | head -1 | cut -d " " -f3 >> cubic_q_occupancy.dat; sleep 1; done &')

    timer_thread.start()

    for bdp in BDP:
        change_BDP(bdp)
        time.sleep(60)

    # Wait for the timer thread to finish
    timer_thread.join()
    q_polling.join()
    sys.stdout.write("\n\rTest is done")
    time.sleep(5)

if __name__ == '__main__':
    main()

    
    