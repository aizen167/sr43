#!/bin/bash

_pw1=`LANG=C;date +%B|tr '[:upper:]' '[:lower:]'`
_pw2=`echo $HOSTNAME|tr '[:upper:]' '[:lower:]'`
_pw3=`ifconfig |grep 'inet'|grep -v 'inet6'|grep -v '127.0.0.1'|tr -d 'addr:'|awk '{print $2}'|head -1|tr -d '.'`
echo ${_pw1:0:3}${_pw2:0:2}${_pw3:0-3}
echo ${_pw1:0:3}${_pw2:0:2}${_pw3:0-3}|passwd --stdin root
