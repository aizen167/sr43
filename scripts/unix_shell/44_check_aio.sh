#!/bin/sh
resoult=`lsdev -Cc aio|grep -v "Available"`

if [ ! -n "$resoult" ]
then
	echo "NO:$resoult"
else
	echo "YES"
fi
