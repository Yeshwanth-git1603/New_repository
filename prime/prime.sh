#!/usr/bin/bash

read -p "enter the num " x
c=0
for i in {1..x+1}
do
	z -eq $x % $i | bc
	if [ $z -eq  0 ]
	then
		c=$((c+1))
	
	if [ $c -eq 2 ]
	then
		echo "prime $x "
	else
		echo "not prime $x "
	fi
	fi
done




