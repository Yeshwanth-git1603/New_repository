#!/usr/bin/bash

for x in {1..10}
do
	if [ $((x % 2)) -eq 0 ]
	then
		echo "even $x"
	else
		echo "odd $x"
	fi
done
