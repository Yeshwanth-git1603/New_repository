#!/usr/bin/bash

addition()
{
	x=1
	y=2
	sum=$((x+y))
	echo "the sum of $x and $y is $sum"
}

addition


addition()
{
	m=$1
	n=$2
	sum=$((m+n))
	echo "the sume of $m and $n is $sum"

}
read -p "enter x " x
read -p "enter y " y
addition $x $y
