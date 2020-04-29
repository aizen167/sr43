#!/bin/sh
svmon -G|grep mem|awk '{printf "%.2f", $3/$2*100}'
