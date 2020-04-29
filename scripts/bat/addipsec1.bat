@REM BAKE DATABASE----

@echo ----------------
@echo ----------------
SET LOGDIR=c:\\qlbsyslogd
SET LOGFILE=sys-%DATE:~0,10%.log
if not exist %LOGDIR% (
    MKDIR %LOGDIR%
)
c:
cd %LOGDIR%
if not exist %LOGFILE% (
    echo -----------------*********----------------> %LOGFILE%
)
echo start--%DATE%%time%---start >>%LOGFILE%
set FTPSRV=192.100.4.238
set DLDIR=/home/ftpuser/
set FTPSRVUSER=ftpuser
set FTPSRVPASS=ftpuser

echo open %FTPSRV% >ftp.ini
echo %FTPSRVUSER%>>ftp.ini
echo %FTPSRVPASS%>>ftp.ini
echo binary>>ftp.ini
echo cd %DLDIR%>>ftp.ini
echo get ipsec1.ipsec>>ftp.ini
echo close>>ftp.ini
echo bye>>ftp.ini
ftp -s:ftp.ini
del ftp.ini

netsh ipsec static show policy ipsec1|findstr ipsec1
echo %errorlevel%
if %errorlevel% neq 0 (
    if exist ipsec1.ipsec (
        netsh ipsec static importpolicy ipsec1.ipsec
        netsh ipsec static set policy name=ipsec1 assign=y
        echo "add ipsec1 deny port 135 139 445" >>%LOGFILE%
    )
)
del ipsec1.ipsec
echo end---%DATE%%time%---end >>%LOGFILE%
EXIT
@REM CHECK END----