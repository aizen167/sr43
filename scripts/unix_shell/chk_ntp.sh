#!/bin/sh
echo $(lssrc -ls xntpd|grep active|wc -l)
