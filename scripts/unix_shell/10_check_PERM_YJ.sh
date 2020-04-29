#!/bin/sh
# 1 months ago =
# 30 days * 1 months * 24 hours * 60 minutes * 60 seconds =
# 2592000 seconds.
now=`perl -MPOSIX -le 'print time'`
let threemonthsago="${now}-2592000"
resoult_DH_PERM=`errpt -dH -T PERM | sed -n '$p'| awk   '{if( $int(2) < $int(threemonthsago)  ) print $0}'`
if [  ! -n  "$resoult_DH_PERM"   ]
then
        echo "YES"
else
        echo "NO:$resoult_DH_PERM"
fi