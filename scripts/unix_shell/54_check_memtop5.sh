#!/bin/sh
resoult_1=`ps aux |head -1`
resoult=`ps aux |sort -rnk6 |head -5`
echo "The current top 5 processes of occupant memory :\n $resoult_1 $resoult"
