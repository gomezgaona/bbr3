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

def run_iperf_test(host, flow, dst_IP, duration, cc, d, l, i):
    cmd = f'{host} iperf3 -c {dst_IP} -t {duration}  -C {cc} -J > json_files/h{flow}_{cc}_{d}_{l}out_{i}.json &'
    os.system(cmd)

def change_BDP(BDP, delay):
    btlbw = 1e9
    burst = int(btlbw/250/8)
    limit = int(BDP*btlbw*delay*(1.024**2)/8) # Setting the limit to BDP

    sys.stdout.write(f"\n\rCurrent BDP: {BDP}\n" )
    tbf_cmd = f'tc qdisc change dev s1-eth1 parent 1: handle 2: tbf rate {btlbw} burst {burst} limit {limit}'
    os.system(tbf_cmd)

def change_netem(delay, loss):
    sys.stdout.write(f"\rCurrent delay: {delay*1e3} ms\n" )
    sys.stdout.write(f"\rCurrent loss: {loss}%\n" )
    netem_cmd_s1 = f'tc qdisc change dev s1-eth1 root handle 1: netem delay {delay}s loss {loss}%'
    #netem_cmd_s2 = f'tc qdisc change dev s2-eth1 root handle 1: netem delay {delay/2}s'
   
    os.system(netem_cmd_s1)
    #os.system(netem_cmd_s2)


def main():
    h = '/home/admin/mininet/util/m hs'
    duration = 60
    delay = [2e-3,  20e-3, 40e-3,  60e-3,  80e-3,  100e-3]
    loss = [0.025]
    cc = "bbr"
    #change_BDP(BDP[0])

    # Create a thread for the timer function
    #timer_thread = threading.Thread(target=timer_function, args=(duration,))
    
    flow = 1
    for i in range(1,11):
        for d in delay:
            change_BDP(1, d)
            time.sleep(5)
            for l in loss:
                change_netem(d, l)
                run_iperf_test(f"{h}{flow}", flow, f"10.0.1.{flow}", duration, cc, d, l, i)
                #timer_thread.start()  
                time.sleep(duration + 5)
            # timer_thread.join()
        
    # Wait for the timer thread to finish
    
    sys.stdout.write("\n\rTest is done\n")
    

if __name__ == '__main__':
    main()

    
    