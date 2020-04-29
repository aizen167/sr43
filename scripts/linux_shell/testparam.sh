#!/bin/sh
echo $1
strA="longstr"
strB="long"
strC="short"
if [[ ${strA} =~ "str" ]]
then
    echo 0
else
    echo 1
fi
