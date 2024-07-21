#!/usr/bin/bash


read -p "choose the color(1.violet,2.indigo,3.blue,4.green,5.yellow,6.orange,7.red) " color

case $color in
	1)
		echo "you selelcted violet"
		;;
	2)
		echo "you selected indigo"
		;;
	3)
		echo "you selected blue"
		;;
	4)
		echo "you selelcted green"
		;;
	5)
		echo "you selected yellow"
		;;
	6)
		echo "you selelcted orange"
		;;
	7)
		echo "you selelcted red"
		;;
	*)
		echo "enter the valid option"
		;;
esac
