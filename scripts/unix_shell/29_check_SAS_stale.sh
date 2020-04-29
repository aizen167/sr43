#!/bin/sh
resoult=`lsdev -Cc disk -Sa |awk '$0~"SCSI" || $0~"SAS" {print $1 ',' $2 }' |grep -v "Available" `

if [ ! -n  "$resoult" ]
then
        echo "YES"
else
        echo "NO:$resoult"
fi