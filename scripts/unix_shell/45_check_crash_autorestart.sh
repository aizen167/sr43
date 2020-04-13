#!/bin/sh
resoult=`lsattr -El sys0 |grep autorestart | grep -i 'True'`

if [ ! -n "$resoult" ]
then
	echo "NO:$resoult"
else
	echo "YES"
fi