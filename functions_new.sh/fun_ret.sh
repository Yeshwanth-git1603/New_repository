#!/usr/bin/bash

addition()
{
	x=1
	y=2
	sum=$((x+y))
	return $sum
}

addition
echo $?


multiplication()
{
	echo "the \$0 value is : $0"
	m=$1
	n=$2
	mul=$((m*n))
	return $mul

}
read -p "enter x "  x
read -p "enter y "  y
multiplication $x $y
echo $?




