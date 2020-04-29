#!/bin/sh
resoult=`lsattr -El mem0  | awk '{print $0}'|grep -i "goodsize" `

if [ ! -n  "$resoult" ]
then
        echo "YES"
else
        echo "NO:$resoult"
fi