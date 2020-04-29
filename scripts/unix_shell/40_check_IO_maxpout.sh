#!/bin/sh
resoult=`lsattr -El sys0 |grep maxpout`

echo "$resoult"