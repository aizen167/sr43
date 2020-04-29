#!/bin/bash
release1=$(lsb_release -r 2>/dev/null|cut -d: -f2|awk '{gsub(/ /,"")}')
release2=$(cat /etc/redhat-release|awk '{print $7}')
release=${release1:-${release2}}
if [ -d /var/log/sa ];then
    case ${release:0:1} in
    5)
        swap=$(find /var/log/sa/ -name sar* -mtime -6|xargs sed -n "/kbswp/,/Average/p"|grep Average|\
            awk 'BEGIN {max=0} {if($9>max)max=$9} END {printf "%.2f\n", max}')
        ;;
    *)
        swap=$(find /var/log/sa/ -name sar* -mtime -6|xargs sed -n "/kbswp/,/Average/p"|grep Average|\
            awk 'BEGIN {max=0} {if($4>max)max=$4} END {printf "%.2f\n", max}')
        ;;
    esac
else
    swap=$(free|grep Swap|awk '{printf "%.2f", $3/$2*100'})
fi
echo "${swap}%"
