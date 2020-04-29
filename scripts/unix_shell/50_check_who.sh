#!/bin/sh
resoult=`who -d |grep -vi "exit=0"`

if [ ! -n "$resoult" ]
then
	echo "YES"
else
	echo "NO:$resoult"
fi
