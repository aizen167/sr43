#!/bin/sh
resoult_1=`svmon -P |awk 'NR==3 {print $0}'`
resoult=`svmon -P |awk 'NF==9 && /^ *[0-9][0-9][0-9][0-9]/ && $5!="s" {print $0}' |sort -rnk5 |head `
echo "The current top 10 processes of occupant page space :\n $resoult_1 $resoult"