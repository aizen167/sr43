#!/bin/bash
grep "^PASS_MIN_LEN" /etc/login.defs|awk '{print $2}'
