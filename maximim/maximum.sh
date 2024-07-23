#!/usr/bin/bash

list=(1 2 3 4 5 6 7 8 9 10)
max="${list[0]}"
for x in list
do
	if [ $x -gt max ]
	then
		$max=$x
	return $max
	else
		echo "not found"
	fi
done



