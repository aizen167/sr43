#!/bin/bash
/etc/init.d/vsftpd status >/dev/null 2>&1
echo $?
