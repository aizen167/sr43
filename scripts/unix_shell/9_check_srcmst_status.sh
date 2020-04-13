#!/bin/sh
resoult_src=`ps -ef|grep src | awk 'NR>3{print}'`

if [  "$resoult_src" = ""  ]
then
        echo "YES"
else
        echo "NO:$resoult_src"
fi