#!/bin/sh
echo $(lsvg -o|lsvg -i -l|grep stale|wc -l)
