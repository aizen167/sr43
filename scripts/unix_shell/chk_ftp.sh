#!/bin/sh
echo $(lssrc -t ftp|grep active|wc -l)
