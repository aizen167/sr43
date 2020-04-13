#!/bin/sh
resoult=`lsdev -Cc adapter -Sa |grep "FC" | awk '{print $1 ',' $2}' |grep -v "Available" `

if [ ! -n  "$resoult" ]
then
        echo "YES"
else
        echo "NO:$resoult"
fi