#!/bin/bash
echo "$(pam_tally2|sed '1d'|awk '$2>4'|wc -l)"
