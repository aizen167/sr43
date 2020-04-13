#!/bin/bash
release1=$(lsb_release -r 2>/dev/null|cut -d: -f2|awk '{gsub(/ /,"")}')
release2=$(cat /etc/redhat-release|awk '{print $7}')
release=${release1:-${release2}}
if [ -d /var/log/sa ];then
    case ${release:0:1} in
    5)
        cpu=$(find /var/log/sa/ -name sar* -mtime -6|xargs sed -n "/CPU/,/Average/p"|grep Average|grep all|\
             awk 'BEGIN {min=100} {if($8<min)min=$8} END {printf "%.2f\n", 100-min}')
        ;;
    *)
        cpu=$(find /var/log/sa/ -name sar* -mtime -6|xargs sed -n "/CPU/,/Average/p"|grep Average|\
             awk 'BEGIN {min=100} {if($11<min)min=$11} END {printf "%.2f\n", 100-min}')
        ;;
    esac
else
    cpu=$(vmstat 1 20|sed '1,3d'|awk 'BEGIN {count=0;sum=0;} {count++; sum+=$15} END {printf "%.2f", 100-sum/count}')
fi
echo "${cpu}%"
