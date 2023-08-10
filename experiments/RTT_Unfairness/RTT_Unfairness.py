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

def run_iperf_test(host, flow, dst_IP, duration, cc, BDP):
    
    cmd = f'{host} iperf3 -c {dst_IP} -t {duration}  -C {cc} -J > json_files/h{flow}_{cc}_{BDP}BDP_out.json &'
    os.system(cmd)

def change_BDP(BDP):
    btlbw = 1e9
    delay = 20e-3
    burst = int(btlbw/250/8)
    limit = int(BDP*btlbw*delay*(1.024**2)/8) # Setting the limit to BDP
    sys.stdout.write(f"\rCurrent BDP: {BDP}\n" )

    
    tbf_cmd = f'tc qdisc change dev s12-eth2 root handle 1: tbf rate {btlbw} burst {burst} limit {limit}'
    os.system(tbf_cmd)

def change_delay(delay):
      
    sys.stdout.write(f"\rCurrent delay: {delay}\n" )
    netem_cmd_s1 = f'tc qdisc change dev s1-eth1 root handle 1: netem delay {delay/2}s loss 0.0046%'
    netem_cmd_s2 = f'tc qdisc change dev s2-eth1 root handle 1: netem delay {delay/2}s'
    #tbf_cmd = f'tc qdisc add dev s1-eth1 root tbf rate {btlbw} burst {burst} limit {limit}'
    os.system(netem_cmd_s1)
    os.system(netem_cmd_s2)

def main():
    h = '/home/admin/mininet/util/m hs'
    duration = 60
    BDP = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    delay = 80e-3

    # Change delay in host hs1 
    sys.stdout.write(f"\rAdding {delay} seconds delay to hs2\n" )
    sys.stdout.write(f"\rTotal delay observed from hs2 0.02 seconds + {delay} seconds = 0.1 seconds\n" )
    #netem_cmd_hs2 = f'{h}2 tc qdisc add dev hs2-eth0 root netem delay {delay}s'
    #print(netem_cmd_hs2)
    #os.system(netem_cmd_hs2)
  
    for bdp in BDP:

        change_BDP(bdp)

        # Create a thread for the timer function
        timer_thread = threading.Thread(target=timer_function, args=(duration,))
        flow = 1
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", bdp)
        flow = 2
        run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", bdp)

        timer_thread.start()

        # Wait for the timer thread to finish
        timer_thread.join()
        sys.stdout.write("\rTest is done")
        time.sleep(5)

    '''
    for bdp in BDP:
        # Change the BDP of s1
        change_BDP(bdp)

        # Create a thread for the timer function
        timer_thread = threading.Thread(target=timer_function, args=(duration,))
       
        for flow in range(1, 101):
            if flow < 51:
                run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "bbr", bdp)
            else:
                run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, "cubic", bdp)
        
        # Start the timer thread
        timer_thread.start()

        # Wait for the timer thread to finish
        timer_thread.join()
        sys.stdout.write("\rTest is done")
        time.sleep(5)
    '''

if __name__ == '__main__':
    main()

    
    