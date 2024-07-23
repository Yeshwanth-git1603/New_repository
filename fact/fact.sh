#!/usr/bin/bash

i=1
read -p "enter the number " n
s=1
while [ $i -le $n ]
do
	s=$((s*i))
	i=$((i+1))
done
echo "the fact of n is $s "
