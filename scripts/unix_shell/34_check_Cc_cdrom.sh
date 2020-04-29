#!/bin/sh
resoult=`lsdev -Cc cdrom|grep -v "Available"`

if [ ! -n "$resoult" ]
then
	echo "YES"
else
	echo "NO:$resoult"
fi
