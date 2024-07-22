#!/usr/bin/bash

read_inputs()
{
	read -p "enter first number" a
	read -p "enter second number" b
}

addition()
{
	sum=$((a+b))
	echo "the sum of $a and $b is $sum"
}

subtraction()
{
	sub=$((a-b))
	echo "the sub of $a and $b is $sub"
}

multiplication()
{
	mul=$(($a*$b))
	echo "the mul of $a and $b is $mul"
}

read_inputs
addition
subtraction
multiplication



