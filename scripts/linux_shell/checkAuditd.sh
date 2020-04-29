#!/bin/bash
service auditd status >/dev/null 2>&1
echo $?
