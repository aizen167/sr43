#!/bin/sh
resoult=`lsdev -Cc adapter -Sa |grep -i "ethernet" | awk '{print $2}'|grep -v "Available" `

if [  "$resoult" = ""  ]
then
        echo "YES"
else
        echo "NO:$resoult"
fi
