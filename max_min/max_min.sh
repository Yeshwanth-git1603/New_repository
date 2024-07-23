#!/usr/bin/bash

read -p "enter the first num" a
read -p "enter the second num" b
read -p "enter the third num " c

if [ $a -gt $b -a $a -gt $c ]
then
	echo "$a is maximum"
elif [ $b -gt $c ]
then
	echo "$b is maximum"
else
	echo "$c is maximum"
fi
