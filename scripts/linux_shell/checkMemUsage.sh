#!/bin/bash
if [  -d /var/log/sa ]
then
    mem=$(find /var/log/sa/ -name sar* -mtime -6|xargs sed -n "/mem/,/Average/p"|grep Average|\
         awk 'BEGIN {max=0} {if($4>max)max=$4} END {printf "%.2f\n", max}')
else
    mem=$(free|grep Mem|awk '{printf "%.2f", $3/$2*100'})
fi
echo "${mem}%"
