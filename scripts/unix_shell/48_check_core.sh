#!/bin/sh
resoult=`ls -l /var/adm/ras/ |grep -i core`

if [ ! -n "$resoult" ]
then
	echo "YES"
else
	echo "NO:$resoult"
fi
