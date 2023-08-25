#!/bin/bash
cc=$1
delay=$2
# Bridge to the HW interface
# sudo ifconfig ens192 10.0.0.10/24
# sudo ifconfig ens192 up

# ss -tin

rm results/"$cc"_"$delay".dat
h='/home/admin/mininet/util/m hs'
while [ 1 ]; do
    #line=`$h1 ss src 10.0.0.1 -tin `
    line=`/home/admin/mininet/util/m hs1 ss -tin src 10.0.0.1 | head -3 |tail -1`
    bw_value=$(echo "$line" | grep -o "bw:[0-9]\+bps" | sed 's/bw:\([0-9]\+\)bps/\1/')
    echo $bw_value
    #echo $bw_value >>line.dat
    echo "$bw_value" >> results/"$cc"_"$delay".dat
    sleep 0.1
done
