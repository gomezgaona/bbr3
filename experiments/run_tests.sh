#!/bin/bash

m="/home/gomezgaj/mininet/util/m"

# Hosts
h1="/home/gomezgaj/mininet/util/m h1"
h2="/home/gomezgaj/mininet/util/m h2"
h3="/home/gomezgaj/mininet/util/m h3"
h4="/home/gomezgaj/mininet/util/m h4"
h5="/home/gomezgaj/mininet/util/m h5"
h6="/home/gomezgaj/mininet/util/m h6"
h7="/home/gomezgaj/mininet/util/m h7"
h8="/home/gomezgaj/mininet/util/m h8"

# TCP buffer size
$h1 "sudo sysctl -w net.ipv4.tcp_wmem='10240 87380 2000000000'"
$h1 "sudo sysctl -w net.ipv4.tcp_rmem='10240 87380 2000000000'"

$h2 "sudo sysctl -w net.ipv4.tcp_wmem='10240 87380 2000000000'"
$h2 "sudo sysctl -w net.ipv4.tcp_rmem='10240 87380 2000000000'"

$h3 "sudo sysctl -w net.ipv4.tcp_wmem='10240 87380 2000000000'"
$h3 "sudo sysctl -w net.ipv4.tcp_rmem='10240 87380 2000000000'"

$h4 "sudo sysctl -w net.ipv4.tcp_wmem='10240 87380 2000000000'"
$h4 "sudo sysctl -w net.ipv4.tcp_rmem='10240 87380 2000000000'"

$h5 "sudo sysctl -w net.ipv4.tcp_wmem='10240 87380 2000000000'"
$h5 "sudo sysctl -w net.ipv4.tcp_rmem='10240 87380 2000000000'"

$h6 "sudo sysctl -w net.ipv4.tcp_wmem='10240 87380 2000000000'"
$h6 "sudo sysctl -w net.ipv4.tcp_rmem='10240 87380 2000000000'"

$h7 "sudo sysctl -w net.ipv4.tcp_wmem='10240 87380 2000000000'"
$h7 "sudo sysctl -w net.ipv4.tcp_rmem='10240 87380 2000000000'"

$h8 "sudo sysctl -w net.ipv4.tcp_wmem='10240 87380 2000000000'"
$h8 "sudo sysctl -w net.ipv4.tcp_rmem='10240 87380 2000000000'"


# Set RTT Unfairness
#$h2 'tc qdisc del dev h2-eth0 root'
#$h2 'tc qdisc add dev h2-eth0 root netem delay 30ms'

#Run iperf3
$h1 "iperf3 -c 20.0.0.1 -t 60 -J -C bbr > out1.json &"
sleep 30
$h2 "iperf3 -c 20.0.0.2 -t 30 -J -C bbr > out2.json "
#sleep 20
#$h3 "iperf3 -c 20.0.0.3 -t 40 -J -C bbr  > out3.json &"
#sleep 20
#$h4 "iperf3 -c 20.0.0.4 -t 20 -J -C bbr  > out4.json &"

#sleep 40
#$h4 "iperf3 -c 20.0.0.4 -t 200 -J -C bbr  > out4.json &"
#sleep 40
#$h5 "iperf3 -c 20.0.0.5 -t 160 -J -C bbr   > out5.json &"
#sleep 40
#$h6 "iperf3 -c 20.0.0.6 -t 120 -J -C bbr   > out6.json &"
#sleep 40
#$h7 "iperf3 -c 20.0.0.7 -t 80 -J -C bbr   > out7.json &"
#sleep 40
#$h8 "iperf3 -c 20.0.0.8 -t 40 -J -C bbr   > out8.json &"
