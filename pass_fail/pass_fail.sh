#!/usr/bin/bash

read -p "enter maths marks " m
read -p "enter physics marks " p
read -p "enter chemistry marks " c

if [ $m -lt 35 -o $p -lt 35 -o $c -lt 35 ]
then
	echo "student is failed $((m+p+c))"
else
	echo "student is passed "
	total=$((m+p+c))
	echo "total marks of the student is $total"
	average=$((total/3))
	echo "the avg marks of the student is $average"
fi

