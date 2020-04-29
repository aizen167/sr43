#!/bin/sh
resoult=`lsdev -C |awk '$2!="Available" && $3~"-"  {print $0}'|grep -v "Available"|grep -v -E "en[0-9]" `

if [ ! -n "$resoult" ]
then
	echo "YES"
else
	echo "NO:$resoult"
fi
