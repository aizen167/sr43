#!/bin/sh
resoult=`lsdev -Cc if | awk '{print $2 ',' $1}'|grep -v "Available" `

if [ ! -n  "$resoult" ]
then
        echo "YES"
else
        echo "NO:$resoult"
fi