#!/usr/bin/bash
read -p "enter the num" n
sum=0
for i in {1..10}
do
	sum=$(( sum + i ))
	echo "the sum is $sum "

done

