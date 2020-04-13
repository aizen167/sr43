#!/bin/sh
echo $(df -Pg|sed '1d'|awk 'BEGIN{ count=0 } { gsub("%","",$5); if($5 > 90){ count++; printf $6 " used " $5 "% " } }\
    END{ if (count == 0){ print "all less 90%" } }')
