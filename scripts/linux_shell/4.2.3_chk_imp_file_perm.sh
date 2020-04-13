#!/bin/bash
for i in /etc/passwd /etc/group /etc/services
do
    if [ -e $i ] && [ $(stat -c %a $i) -gt 644 ];then echo $i;fi
done
for i in {0..6}
do
	if [ -e $i ] && [ $(stat -c %a /etc/rc${i}.d) -gt 750 ];then echo /etc/rc${i}.d;fi
done
for i in /etc/ /etc/rc.d/init.d/ /tmp/
do
    if [ -e $i ] && [ $(stat -c %a $i) -gt 750 ];then echo $i;fi
done
for i in /etc/grub.conf /etc/xinetd.conf /etc/security
do
    if [ -e $i ] && [ $(stat -c %a $i) -gt 600 ];then echo $i;fi
done
for i in /etc/shadow
do
    if [ -e $i ] && [ $(stat -c %a $i) -gt 400 ];then echo $i;fi
done
