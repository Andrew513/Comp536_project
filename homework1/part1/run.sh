#!/bin/bash

rm -f result.txt

for i in {1..1000}
do
    ./prog | grep -E "f1|f2" | tr -d '\n' >> result.txt
    echo "" >> result.txt
done

sort result.txt | uniq -c