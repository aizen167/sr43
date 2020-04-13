#!/bin/sh
resolut=`netstat -in | grep -i "en"   |awk '{if(int($6==0) && int($8==0)) print $1 ',' $6 ',' $8}`'

if [ ! -n  "$resoult" ]
then
        echo "YES"
else
        echo "NO:$resoult"
fi