#!/bin/sh
resoult_err=`ps -ef|grep err | awk 'NR>3{print}'`
if [  "$resoult_err" = ""  ]
then
        echo "YES"
else
        echo "NO:$resoult_err"
fi
