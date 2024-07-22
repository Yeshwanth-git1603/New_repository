#!/usr/bin/bash

read_inputs()
{
	m=$1
	n=$2
	sum=$((m+n))
	echo "the value of $m and $n is $sum"
}

subtraction()
{
	m=$1
	n=$2
	sub=$((m-n))
	echo "the value of $m and $n is $sub"
}
x=10
y=20
read_inputs $x $y

p=5
q=9
subtraction $p $q
