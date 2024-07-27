#!/usr/bin/bash

factorial()
{
	n=1$
	if [ $n -eq 0 ]
	then
		return 1
	else
		return $(($n*factorial))$(($n-1))
	fi

}
x=5
factorial $x
echo $?


