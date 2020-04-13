#!/bin/sh
echo $(lsuser -a unsuccessful_login_count ALL|grep unsuccessful_login_count|grep -v guest|awk -F "=" '$2>4'|wc -l)
