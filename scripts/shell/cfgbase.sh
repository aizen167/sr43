#!/bin/bash

#****************************************************************
# this shell is for config baseline
# 
#****************************************************************

# Set server ip address
_set_server () {
	servlist="192.100.4.238 172.18.248.248 192.100.5.239 192.168.168.17"
	server=192.100.4.238
	for i in $servlist
	do
    	ping -c1 $i >/dev/null 2>&1
    	if [ $? -eq 0 ]
    	then
        	server=$i
        	break
    	fi
	done
}

# Get os release
_get_release () {
	release1=$(lsb_release -r 2>/dev/null|cut -d: -f2|awk '{gsub(/ /,"")}')
	release2=$(cat /etc/redhat-release|awk '{print $7}')
	release=${release1:-${release2}}
}

# Get IP address
_get_IP () {
    ip1=$(ifconfig |grep 'inet'|grep -v 'inet6'|grep -v '127.0.0.1'|tr -d 'addr:'|awk '{print $2}'|head -1)
    ip2=$(grep "$HOSTNAME" /etc/hosts|awk '{print $1}')
    ip=${ip1:-${ip2}}
    if [ -z ${ip} ]
    then
        echo "ip addr is null,exit"
    else
        echo "IP addr: ${ip}"
    fi
}

#****************************************************************
# start of function for baseline
#****************************************************************
#Stop services not used
_stopserv () {
    for i in avahi-daemon bluetooth cups hplip ip6tables iptables \
             iscsi iscsid isdn kudzu pcscd rhnsd rhsmcertd rpcgssd \
             rpcidmapd sendmail yum-updatesd telnet firewalld
    do
        service $i stop >/dev/null 2>&1
        chkconfig $i off >/dev/null 2>&1
    done
}

# Disable selinux
_disable_selinux () {
    sed -i "s/SELINUX=enforcing/SELINUX=disabled/g" /etc/selinux/config
}

# Config ntp
_cfg_ntp () {
    local ntpservlist="192.1.7.77 172.18.248.200"
    local ntpserver=192.1.7.77
    for i in $ntpservlist
    do
        ping -c1 $i >/dev/null 2>&1
        if [ $? -eq 0 ]
        then
            ntpserver=$i
            break
        fi
    done
    ! grep "datesrv" /etc/hosts >/dev/null 2>&1 && sed -i "$ a ${ntpserver} datesrv" /etc/hosts
    case ${release} in 
    7*)
        yum -y install chrony
        grep datesrv /etc/chrony.conf >/dev/null 2>&1
        if [ $? -ne 0 ]
        then
            #add # to the old three server
            sed -i "s/^server/#server/g" /etc/chrony.conf
            #add the new server
            sed -i "$ a server datesrv iburst" /etc/chrony.conf
        fi
        systemctl restart chronyd
        systemctl enable chronyd
        ;;
    6*)
        yum -y install ntp
        grep datesrv /etc/ntp.conf >/dev/null 2>&1
        if [ $? -ne 0 ]
        then
            #add # to the old three server
            sed -i "s/^server/#server/g" /etc/ntp.conf
            #add the new server
            sed -i "$ a server datesrv" /etc/ntp.conf
        fi
        ;;
    esac
}

_disable_control_alt_delete () {
    case ${release} in 
    7*)
        rm -f /usr/lib/systemd/system/ctrl-alt-del.target && init q
        ;;
    6*)
        sed -i "s/exec/\#exec/" /etc/init/control-alt-delete.conf
        ;;
    *)
        sed -i "s/exec/\#exec/" /etc/init/control-alt-delete.conf
        ;;
    esac
}

_4_1_1_cfg_login_defs () {
    sed -i "/^PASS_MAX_DAYS/c PASS_MAX_DAYS   90" /etc/login.defs
    sed -i "/^PASS_MIN_DAYS/c PASS_MIN_DAYS   7" /etc/login.defs
    sed -i "/^PASS_MIN_LEN/c PASS_MIN_LEN    8" /etc/login.defs
    sed -i "/^PASS_WARN_AGE/c PASS_WARN_AGE   0" /etc/login.defs
    sed -i "/^UMASK/c UMASK   027" /etc/login.defs
}

_4_2_2_cfg_umask () {
    for i in /etc/profile /etc/bashrc /etc/csh.cshrc
    do
        sed -r 's/(^[[:blank:]]*umask)[^*]*/\1 027/' --in-place $i
    done
}

_4_2_3_cfg_imp_file_perm () {
    for i in /etc/passwd /etc/group /etc/services
    do
        chmod 644 $i
    done
    for i in {0..6}
    do
        chmod 750 /etc/rc${i}.d
    done
    for i in /etc/rc.d/init.d/
    do
        chmod 750 $i
    done
    for i in /etc/grub2.cfg /etc/xinetd.conf /etc/security
    do
        chmod 600 $i
    done
    for i in /etc/shadow
    do
        chmod 400 $i
    done
}

_4_2_9_cfg_su () {
    grep "root_only" /etc/pam.d/su
    if [ $? -ne 0 ]
    then
        sed -i "6 s/#//" /etc/pam.d/su
        #sed -i "6 s/use_uid/use_uid root_only group_wheel/g" /etc/pam.d/su
    fi
}

_4_3_cfg_passwd_policy () {
    case ${release} in 
    7*)
		#authconfig --enablereqlower --update
		#authconfig --enablereqdigit --update
		authconfig --passminlen=8 --update
		authconfig --passminclass=3 --update
        ;;
    *)
    	grep "pam_cracklib.so" /etc/pam.d/system-auth
    	if [ $? -ne 0 ]
    	then
        	sed -i "/pam_cracklib.so/c password    requisite     pam_cracklib.so lcredit=-2 dcredit=-1" /etc/pam.d/system-auth
    	fi
        ;;
    esac
}

_4_3_cfg_passwd_lock () {
    grep "pam_tally2.so" /etc/pam.d/system-auth
    if [ $? -ne 0 ]
    then
        sed -i "/pam_env/i auth        required      pam_tally2.so deny=5 unlock_time=300" /etc/pam.d/system-auth
    fi

    grep pam_tally2.so /etc/pam.d/password-auth
    if [ $? -ne 0 ]
    then
        sed -i "/pam_env/i auth        required      pam_tally2.so deny=5 unlock_time=300" /etc/pam.d/password-auth
    fi
}

_4_3_cfg_passwd_remember () {
    grep remember /etc/pam.d/system-auth
    if [ $? -ne 0 ]
    then
        sed -i "s/use_authtok/use_authtok remember=12/" /etc/pam.d/system-auth
    fi
}
_cfg_tmout () {
    grep TMOUT /etc/profile >/dev/null 2>&1
    if [ $? -ne 0 ]
    then
        sed -i "$ a export TMOUT=900" /etc/profile
    fi
}

_install_rpm () {
    yum -y install unzip
    yum -y install sysstat
    yum -y install net-tools
}
#****************************************************************
# end of function for baseline
#****************************************************************

#****************************************************************
# config yum.repo
#****************************************************************
_cfg_yum () {
    ! grep "yum.qlbchina.com" /etc/hosts >/dev/null 2>&1 && sed -i "$ a ${server} yum.qlbchina.com" /etc/hosts
    curl -s -O http://${server}/rc/other/rhel-${release:0:1}-server-rpms.repo
    mv rhel-${release:0:1}-server-rpms.repo /etc/yum.repos.d/
    local yumfile=/etc/yum.repos.d/Rhel-Base.repo
    echo "[os]" >${yumfile}
    echo 'name=Red Hat Enterprise Linux $releasever - $basearch - Source' >>${yumfile}
    echo "baseurl=http://yum.qlbchina.com/yum/rhel/${release}/os/\$basearch/" >>${yumfile}
    echo "enabled=1" >>${yumfile}
    echo "gpgcheck=0" >>${yumfile}
    echo "gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release" >>${yumfile}
    echo "" >>${yumfile}
    echo "[extra]" >>${yumfile}
    echo 'name=Red Hat Enterprise Linux $releasever - $basearch - Source' >>${yumfile}
    echo 'baseurl=http://yum.qlbchina.com/yum/rhel/$releasever/extra/$basearch/' >>${yumfile}
    echo "enabled=1" >>${yumfile}
    echo "gpgcheck=0" >>${yumfile}
    echo "gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release" >>${yumfile}
    echo "" >>${yumfile}
    yum clean all >/dev/null 2>&1
    yum makecache >/dev/null 2>&1
}
#****************************************************************
# end config yum.repo
#****************************************************************

#Backup files before changed
_backup () {
	local backupdir=/root/basebak/$(date +%y%m%d.%H%M%S)
	[ ! -d $backupdir ] && mkdir -p $backupdir
	cp /etc/profile /etc/selinux/config /etc/hosts /etc/login.defs $backupdir 2>/dev/null
	cp /etc/ntp.conf /etc/init/control-alt-delete.conf $backupdir 2>/dev/null
	cp /etc/pam.d/su /etc/pam.d/system-auth /etc/pam.d/password-auth $backupdir 2>/dev/null
}

pre_ora () {
    ### add user and group ###
    groupadd -g 500 oinstall
    groupadd -g 501 dba
    useradd -g 500 -G 501 -u 500 -d /oracle oracle && echo "oracle"|passwd --stdin oracle
    yum -y install binutils
    yum -y install compat-libstdc++-33
    yum -y install elfutils-libelf
    yum -y install elfutils-libelf-devel
    yum -y install glibc
    yum -y install glibc-common
    yum -y install glibc-devel
    yum -y install gcc
    yum -y install gcc-c++
    yum -y install libaio
    yum -y install libaio-devel
    yum -y install libgcc
    yum -y install libstdc++
    yum -y install libstdc++-devel
    yum -y install libXp
    yum -y install make
    yum -y install sysstat
    yum -y install unixODBC
    yum -y install unixODBC-devel
    yum -y install pdksh
    echo "the results of installation:"
    rpm -q --qf '%{NAME}-%{VERSION}-%{RELEASE}(%{ARCH})\n' binutils \
    compat-libstdc++-33 gcc gcc-c++ glibc glibc-common \
    libstdc++ libstdc++-devel libXp make pdksh sysstat
}

pre_db2 () {
    yum -y install libstdc++.i686
    yum -y install sg3_utils.x86_64
    yum -y install pam.i686
    rpm -q --qf '%{NAME}-%{VERSION}-%{RELEASE}(%{ARCH})\n' libstdc++ sg3_utils pam
}

pre_wls () {
	groupadd -g 600 bea
	useradd -g 600 -u 600 -d /weblogic weblogic && echo "weblogic"|passwd --stdin weblogic
}

ins_zabbix () {
	rpm -q zabbix-agent || yum -y install zabbix-agent >/dev/null
	curl -s -o /etc/zabbix/zabbix_agentd.conf http://${server}/rc/zbx/conf/zabbix_agentd.conf
	curl -s -o /etc/zabbix/zabbix_agentd.d/userparameter.conf http://${server}/rc/zbx/conf/userparameter.conf
	curl -s -o /etc/zabbix/zabbix_agentd.d/mq.conf http://${server}/rc/zbx/conf/mq.conf
	curl -s -o /tmp/zbxscripts.tar http://${server}/rc/zbx/scripts/zbxscripts.tar
	[ -e /tmp/zbxscripts.tar ] && tar xvf /tmp/zbxscripts.tar -C /usr/local/bin/
	case ${release} in
	7*)
    	systemctl enable zabbix-agent
    	;;
	6*)
    	chkconfig --add zabbix-agent
    	chkconfig zabbix-agent on
    	;;
	*)
    	chkconfig --add zabbix-agent
    	;;
	esac
	service zabbix-agent restart >/dev/null
}

ins_av () {
	curl -s -o /tmp/kingsoft.tar.gz http://${server}/rc/av/kingsoft.tar.gz
	[ -e /tmp/kingsoft.tar.gz ] && tar zxvf /tmp/kingsoft.tar.gz -C /tmp/
	cd /tmp/kingsoft && sh install.sh -s 172.18.253.63 -p /opt/kingsoft -c ${ip}
}

cfg_syslog () {
	curl -s -o linux-syslog.conf http://${server}/rc/other/linux-syslog.conf
	[ -e linux-syslog.conf ] && mv linux-syslog.conf /etc/rsyslog.d/
	service rsyslog restart
}

cfg_base () {
	_backup
	_cfg_yum
	_install_rpm
	_disable_selinux
	_cfg_tmout
	_cfg_ntp
	_disable_control_alt_delete
	_stopserv
	_4_1_1_cfg_login_defs
	_4_2_2_cfg_umask
	_4_2_3_cfg_imp_file_perm
	_4_2_9_cfg_su
	_4_3_cfg_passwd_policy
	_4_3_cfg_passwd_lock
	_4_3_cfg_passwd_remember
}

main () {
	_set_server
	_get_release
	_get_IP
	if [ $# -eq 0 ]; then
		cfg_base
		read -n1 -p "Do you want to install rpm for Graphical[y/n]" isGraphical
		case ${isGraphical} in
		Y|y|YES|yes)
    		yum -y install xorg-x11-utils
    		;;
		*)
    		echo "do nothing"
			;;
		esac
		read -n1 -p "Do you want to install rpm for Oracle [y/n]" isOracle
		case ${isOracle} in
		Y|y|YES|yes)
			pre_ora
    		;;
		*)
    		echo "do nothing"
    		;;
		esac
		read -n1 -p "Do you want to install rpm for DB2 [y/n]" isDB2
		case ${isDB2} in
		Y|y|YES|yes)
			pre_db2
    		;;
		*)
    		echo "do nothing"
    		;;
		esac
	else while [ $# -ne 0 ]; do
		case "$1" in
		--base)
			cfg_base
			shift
			;;
		--yum)
			_cfg_yum
			shift
			;;
		--slg)
			cfg_syslog
			shift
			;;
		--gra)
    		yum -y install xorg-x11-utils
			shift
			;;
		--ora)
    		pre_ora
			shift
			;;
		--db2)
    		pre_db2
			shift
			;;
		--wls)
    		pre_wls
			shift
			;;
		--zbx)
    		ins_zabbix
			shift
			;;
		--av)
    		ins_av
			shift
			;;
		*)
			return 1
			;;
		esac
		done
	fi
}

main "$@"

#rm itself
#rm -- "$0"
