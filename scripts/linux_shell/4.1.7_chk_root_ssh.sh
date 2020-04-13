#!/bin/bash
grep "^PermitRootLogin" /etc/ssh/sshd_config|awk '{print $2}'
