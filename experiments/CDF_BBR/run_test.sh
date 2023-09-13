#!/bin/bash
cc=$1
delay=$2
# Bridge to the HW interface
# sudo ifconfig ens192 10.0.0.10/24
# sudo ifconfig ens192 up

# ss -tin

rm results/"$cc"_"$delay"_hw.dat
h='/home/admin/mininet/util/m hs'
#while [ 1 ]; do
    #line=`$h1 ss src 10.0.0.1 -tin `
    line_1=` ss -tin src 10.0.0.10 | tail -1`
    line_2=` ss -tin src 10.0.0.10 | tail -3 | head -1`
    line_3=` ss -tin src 10.0.0.10 | tail -5 | head -1`
    line_4=` ss -tin src 10.0.0.10 | tail -7 | head -1`
    #line_1=`cat "temp.dat" | tail -1` > /dev/null
    #line_2=`cat "temp.dat" | tail -3 | head -1`> /dev/null
    #line_3=`cat "temp.dat" | tail -5 | head -1`> /dev/null
    #line_4=`cat "temp.dat" | tail -7 | head -1`> /dev/null
   
    bw_value_1=$(echo "$line_1" | grep -o "bw:[0-9]\+bps" | sed 's/bw:\([0-9]\+\)bps/\1/')
    bw_value_2=$(echo "$line_2" | grep -o "bw:[0-9]\+bps" | sed 's/bw:\([0-9]\+\)bps/\1/')
    bw_value_3=$(echo "$line_3" | grep -o "bw:[0-9]\+bps" | sed 's/bw:\([0-9]\+\)bps/\1/')
    bw_value_4=$(echo "$line_4" | grep -o "bw:[0-9]\+bps" | sed 's/bw:\([0-9]\+\)bps/\1/')
    echo $bw_value_1
    echo $bw_value_2
    echo $bw_value_3
    echo $bw_value_4
    total_bw=$(($bw_value_1 + $bw_value_2  + $bw_value_3 + $bw_value_4))
    echo $total_bw
    #echo $total_bw
    #echo $bw_value >>line.dat
    echo "$total_bw" >> results/"$cc"_"$delay"_hw.dat
    sleep 0.1
#done
