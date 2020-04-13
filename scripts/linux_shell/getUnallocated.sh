#!/bin/bash
echo $(/sbin/vgs|sed '1d'|awk 'BEGIN{count=0} {if($7 >0) {print $1 "  " $7; count++}} END{if(count==0) print "none"}')
