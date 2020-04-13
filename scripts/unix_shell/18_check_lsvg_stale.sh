#!/bin/sh
resoult_vg_stale=`lsvg -o |lsvg -i -l |grep -i stale `

if [  ! -n  "$resoult_vg_stale"   ]
then
        echo "YES"
else
        echo "NO:$resoult_vg_stale"
fi