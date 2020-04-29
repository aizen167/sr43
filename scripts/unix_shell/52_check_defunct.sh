#!/bin/sh
echo " The current zombie processes is : (one time per 5 second)"
 for i in first second third forth fifth
 do
 echo " the $i check: "
 ps -ef |grep defunct|grep -vi grep
 sleep 5
 echo 
 done