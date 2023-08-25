#!/bin/bash
cc=$1
delay=$2
# Bridge to the HW interface
sudo ifconfig ens192 10.0.0.10/24
sudo ifconfig ens192 up

sudo sysctl -w net.ipv4.tcp_wmem='10240 87380 2000000000'
sudo sysctl -w net.ipv4.tcp_rmem='10240 87380 2000000000'

# ss -tin

#Run iperf3
pkill iperf3
iperf3 -c 20.0.0.10 -t 120 -J -C $cc > results/"$cc"_"$delay".json &

rm results/"$cc"_"$delay".dat
while [ 1 ]; do
    line=`ss -tin src 10.0.0.10 | tail -1`
    bw_value=$(echo "$line" | grep -o "bw:[0-9]\+bps" | sed 's/bw:\([0-9]\+\)bps/\1/')
    echo "$bw_value" >> results/"$cc"_"$delay".dat
    sleep 0.1
done
