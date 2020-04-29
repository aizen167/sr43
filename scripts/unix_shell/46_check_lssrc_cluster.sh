#!/bin/sh
resoult=`lssrc –g cluster | grep -v 'active'`

if [ ! -n "$resoult" ]
then
	echo "NO:$resoult"
else
	echo "YES"
fi