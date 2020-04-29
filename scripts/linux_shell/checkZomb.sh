#!/bin/bash
#echo $(ps -elf|awk '$2 ~ "Z"'|wc -l)
echo $(ps -ef|grep defunct|grep -v grep|wc -l)
