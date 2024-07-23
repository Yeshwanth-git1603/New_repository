#!/usr/bin/bash

for x in {1..10}
do
	sum=$((x * x + 1/2))
	echo "sum is $sum"
done
