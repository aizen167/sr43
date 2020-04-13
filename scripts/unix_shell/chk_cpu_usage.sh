#!/bin/sh
echo $(vmstat 1 10|sed '1,6d'|awk 'BEGIN{max=0}{if($14>max)max=$14}END{print max}')"%"
