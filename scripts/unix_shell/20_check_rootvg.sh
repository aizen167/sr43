#!/bin/sh
rm -rf /tmp/check_rootvg.txt
for LV in `lsvg -l rootvg |awk 'NR>2 {print $1}'`
do
resoult_rootvg=`getlvcb -lcs $LV |awk '{ if(int($1)!=2 )   printf("%18s\t%d\t%s\n",$2,$1,$3)}' >> /tmp/check_rootvg.txt`
done
resoult=` cat /tmp/check_rootvg.txt | grep -v '2' `

if [ ! -n "$resoult" ]
then
	echo "NO:$resoult"
else
	echo "YES"
fi
rm -rf /tmp/check_rootvg.txt