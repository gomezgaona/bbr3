#!/bin/bash
arrival_times=`python3 -c 'from generate_arrival_time_poisson import *; print (" ".join(gen()))'`

i=1
pkill tcpdump > /dev/null 2>&1

tcpdump -i hs1-eth0 -w "$1".pcap 'port 80'  &

#sleep 1


for curr_time in $arrival_times:
do
	echo "flow: $i"
	#wget -T 5 --delete-after 50.0.0.1/gen_files/file$i.html -q  &
	wget --delete-after 10.0.1.1/gen_files/file$i -q &
	pids[${i}]=$!
	sleep $curr_time
	i=$((i+1))
done

# wait for all pids
for pid in ${pids[*]}; do
	wait $pid
done


pkill tcpdump
