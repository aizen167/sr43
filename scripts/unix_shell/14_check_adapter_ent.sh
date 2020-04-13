#!/bin/sh
resoult=`lsdev -Cc adapter |grep ent | awk '{print $2 ',' $1}'|grep -v "Available" `

if [ ! -n  "$resoult" ]
then
        echo "NO:$resoult"
else
        echo "YES"
fi