#!/bin/sh
resoult=`uptime | awk -F"," '{print $1}' |awk '{print $3}'`

echo "$resoult"