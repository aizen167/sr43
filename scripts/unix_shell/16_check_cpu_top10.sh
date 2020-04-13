#!/bin/sh
 echo "The current top 10 processes of occupant cpu:\n "
 i=1
 while [ $i -le 5 ]
 do
 ps -ef |head -1
 ps -ef |grep -v "^UID" |sort -rnk4 |head -10
 sleep 2
 echo 
 let i=$i+1
 done