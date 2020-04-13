#!/bin/sh
resoult_lsps_swap=`lsps -s | grep -v  "Percent Used" | awk '{if(int($2 >=20)) print $0}' `

if [  ! -n  "$resoult_lsps_swap"   ]
then
        echo "YES"
else
        echo "NO:$resoult_lsps_swap"
fi