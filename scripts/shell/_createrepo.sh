#!/bin/bash

for i in {6..7}
do
	cd /var/www/html/yum/rhel-${i}-server-rpms/
	createrepo /var/www/html/yum/rhel-${i}-server-rpms/ -g comps.xml
	file=$(ls -t *.updateinfo.xml.gz|head -1|awk '{print $1}'
	if [ -e ${file} ];then
		gunzip ${file}
		mv ${file%.*} /var/www/html/yum/rhel-${i}-server-rpms/repodate/updateinfo.xml
	modifyrepo /var/www/html/yum/rhel-${i}-server-rpms/repodata/updateinfo.xml /var/www/html/yum/rhel-${i}-server-rpms/repodata
done
