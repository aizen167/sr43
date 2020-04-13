#!/bin/bash
echo $(egrep -i 'error|crit|alert|panic|fail' /var/log/messages|wc -l)
