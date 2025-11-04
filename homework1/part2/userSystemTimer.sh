#!/usr/bin/env bash
set -euo pipefail

rm -f v1_user.txt v1_sys.txt v2_user.txt v2_sys.txt

for i in {1..1000}; do
  # prints: "<user> <sys>"
  gtime -f "%U %S" ./ver1 1>/dev/null 2>> v1_raw.txt
  gtime -f "%U %S" ./ver2 1>/dev/null 2>> v2_raw.txt
done

awk '{print $1}' v1_raw.txt > v1_user.txt
awk '{print $2}' v1_raw.txt > v1_sys.txt
awk '{print $1}' v2_raw.txt > v2_user.txt
awk '{print $2}' v2_raw.txt > v2_sys.txt
