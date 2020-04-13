#!/bin/sh
for vg in $(lsvg -o)
do
    echo "${vg} left $(lsvg ${vg}|grep -i "free pps"|cut -d '(' -f2|cut -d ')' -f1)"
done
