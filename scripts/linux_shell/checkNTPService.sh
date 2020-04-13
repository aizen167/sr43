#!/bin/bash
if [[ $1 =~ ntp ]];then
    echo 0
else
    service ntpd status >/dev/null 2>&1 || service chronyd status >/dev/null 2>&1
    echo $?
fi
