#!/bin/bash
### install
/weblogic/Oracle/Middleware/utils/bsu/bsu.sh -install -patch_download_dir=/weblogic/Oracle/Middleware/utils/bsu/cache_dir \
-patchlist=MXLE -prod_dir=/weblogic/Oracle/Middleware/wlserver_10.3 -verbose
### remove
/weblogic/Oracle/Middleware/utils/bsu/bsu.sh -remove -patchlist=U5I2 -prod_dir=/weblogic/Oracle/Middleware/wlserver_10.3 -verbose
### view
/weblogic/Oracle/Middleware/utils/bsu/bsu.sh -view -prod_dir=/weblogic/Oracle/Middleware/wlserver_10.3 -status=applied -verbose
