#!/bin/sh
resoult=`lsdev -Cc adapter -Sa |grep -i "raid"`

echo "$resoult"