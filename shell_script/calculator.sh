#!/usr/bin/bash


read -p "enter a value " a
read -p "enter b value"  b
read -p "enter the option(1.add,2.sub,3.mul,4.div) " opt

case $opt in
	1)
		echo "you selected add"
		echo "the value of $a and $b is $((a+b))"
		;;
	2)
		echo "you selected sub"
		echo "the value of $a and $b is $((a-b))"
		;;
	3)
		echo "you selelcted mul"
		echo "the value of $a and $b is $((a*b))"
		;;
	4)
		echo "you selelcted div"
		echo "the value of $a and $b is $(bc<<<"scale=2;$a/$b")"
		;;
	*)
		echo "enter the valid option"
		;;
esac
