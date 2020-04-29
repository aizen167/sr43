#!/bin/bash
users=adm,lp,mail,uucp,operator,games,gopher,ftp,nobody,nobody4,noaccess,listen,webservd,rpm,dbus,avahi,mailnull,smmsp,nscd,vcsa,rpc,rpcuser,nfs,sshd,pcap,ntp,haldaemon,distcache,apache,webalizer,squid,xfs,gdm,sabayon,named
for i in $(IFS=",";echo ${users})
do
    grep -w $i /etc/passwd|grep -v /sbin/nologin && \
    grep $i /etc/shadow|awk -F: '($2 !~ "!") {printf $1" "}'
done
echo "0"
