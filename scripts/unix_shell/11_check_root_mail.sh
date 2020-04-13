#!/bin/sh
resoult_mail=` mail | grep -i "diagela message" `

if [  "$resoult_mail" = ""  ]
then
        echo "YES"
else
        echo "NO:$resoult_mail"
fi