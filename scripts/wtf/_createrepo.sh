#!/bin/bash
cd /var/www/html/yum/rhel-7-server-rpms/
createrepo -v /var/www/html/yum/rhel-7-server-rpms/ -g comps.xml
gunzip *updateinfo.xml.gz
mv *updateinfo.xml /var/www/html/yum/rhel-6-server-rpms/repodate/updateinfo.xml
#modifyrepo /var/www/html/yum/rhel-6-server-rpms/repodata/updateinfo.xml /var/www/html/yum/rhel-6-server-rpms/repodata
modifyrepo /var/www/html/yum/rhel-7-server-rpms/repodata/updateinfo.xml /var/www/html/yum/rhel-7-server-rpms/repodata
