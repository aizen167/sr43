#!/bin/bash

if [[ $1 =~ itm ]];then
    echo 1
else
    echo $(ps -ef|grep -v grep|grep klzagent|wc -l)
fi
