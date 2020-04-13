#!/bin/sh
# 1 months ago =
# 30 days * 1 months * 24 hours * 60 minutes * 60 seconds =
# 2592000 seconds.
now=`perl -MPOSIX -le 'print time'`
let threemonthsago="${now}-2592000"
resoult_DS_PERM=`errpt -dS -T PERM | sed -n '$p'| awk   '{if( $int(2) < $int(threemonthsago)  ) print $0}'`
if [  ! -n  "$resoult_DS_PERM"   ]
then
        echo "YES"
else
        echo "NO:$resoult_DS_PERM"
fi

 