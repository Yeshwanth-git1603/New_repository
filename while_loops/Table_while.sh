#!/usr/bin/bash

read -p "enter the num " a
read -p "enter the table end value to print " b
b=1
while [ $a -lt 10 ]
do
    while [ $b -lt 11 ]
    do
        echo " $a * $b = $(($a*$b))"
        b=`expr $b + 1`
    done
done


