#!/bin/bash
grep "^PASS_WARN_AGE" /etc/login.defs|awk '{print $2}'
