#!/usr/bin/bash


read -p "enter first value "  a
read -p "enter second value "  b

if [$a -gt $b]
then
	echo "$a is greater"
else
	echo "$b is greater"
fi


read -p "enter the first value " a
read -p "enter the second value " b
read -p "enter the third value " c

if [$a -gt $b -a $a -gt $c]
then
	echo "$a is greater"
elif [$b -gt $c]
then
	echo "$b is greater"
else
	echo "$c is greater"
fi
