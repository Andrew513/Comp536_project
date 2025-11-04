#! /bin/bash

rm -f ver1_time.txt ver2_time.txt

TIME_CMD="time"
if command -v gtime &> /dev/null
then
    TIME_CMD="gtime -f %e"
fi

for i in {1..1000}
do
    $TIME_CMD ./ver1 2>> ver1_time.txt
    $TIME_CMD ./ver2 2>> ver2_time.txt
done
