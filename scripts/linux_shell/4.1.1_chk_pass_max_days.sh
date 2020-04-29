#!/bin/bash
grep "^PASS_MAX_DAYS" /etc/login.defs|awk '{print $2}'
