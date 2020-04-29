#!/bin/bash
for part in $(grep -v ^# /etc/fstab|awk '($6="0"){print $2}')
do
    echo $part
    find $part \( -perm -04000 -o -perm -02000 \) -type f -print
done

