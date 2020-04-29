#!/bin/sh
lsps -s|grep -v "Percent"|awk '{print $2}'
