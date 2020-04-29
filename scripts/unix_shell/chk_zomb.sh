#!/bin/sh
echo $(ps -ef|grep defunct|grep -vi grep|wc -l)
