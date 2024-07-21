#!/usr/bin/bash

for i in {1..10}
do
	echo "$i"
done

array=(1 2 3 4 5)
for i in ${array[*]}
do
	echo "$i"
done



for i in {n}
do
	echo "$i"
done



# associative array

ass_array=([name]="yeshwanth" [age]=23 [location]="hyd")

for i in ${ass_array[*]}
do
	echo "$i"
done



for i in $(ls)
do
	echo "$i"
done



for i in $(whereis usr)
do
	echo "$i"
done


