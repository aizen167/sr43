#!/bin/sh
resoult=`lsdev -Cc tape |grep -v "Available"`

if [ ! -n "$resoult" ]
then
	echo "YES"
else
	echo "NO:$resoult"
fi
