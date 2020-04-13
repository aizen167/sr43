#!/bin/sh
resoult=`wc -l /var/hacmp/log/clverify.log | awk '{print }'`

if [ ! -n "$resoult" ]
then
	echo "YES"
else
	echo "NO:$resoult"
fi
