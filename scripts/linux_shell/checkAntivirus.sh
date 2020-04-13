#!/bin/bash
if [[ $1 =~ "av" ]];then
    echo 0
else
    /etc/init.d/KANLinuxClient status >/dev/null 2>&1
    echo $?
fi
