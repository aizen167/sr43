#!/bin/sh

resoult_sysdumpdev=`sysdumpdev -e | grep -i 'size' | awk '{print $7}'`
resoult_size_devsize=`expr $resoult_sysdumpdev / 1024 / 1024 `
resoult_devvar_size=`df -g|grep -i "/var" | awk '{print $2*1024}'` 

if [   "$resoult_size_devsize" > "$resoult_devvar_size"  ]
then
        echo "NO:sysdumpdev:$resoult_size_devsize(MB)"
else
        echo "YES"
fi