#!/bin/bash
find / -maxdepth 3 -name .rhosts 2>/dev/null
find / -maxdepth 3 -name .netrc 2>/dev/null
echo "0"
