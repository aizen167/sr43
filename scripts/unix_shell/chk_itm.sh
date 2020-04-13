#!/bin/bash

if [[ $1 == *itm* ]];then
    echo 2
else
    echo $(ps -ef|grep -E ku[xl]agent|wc -l)
fi
