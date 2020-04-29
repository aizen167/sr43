#!/bin/sh
resoult=`df -g | awk '{if (int($4 > 80)) print $1 ',' $4 }'| sed '1d'|grep -i "" `
if [  ! -n "$resoult" ]
then
	echo "YES"
else
	echo "NO:$resoult"
fi
