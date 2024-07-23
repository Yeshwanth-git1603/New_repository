#!/usr/bin/bash

read -p "Enter a number : " n
i=1
c=0
while [ $i -le $n ]
do
        rem=$(($n % $i))
        if [ $rem -eq 0 ]
        then
                let c++
        fi
        let i++
done
if [ $c -eq 2 ]
then
        echo "Prime Number"
else
        echo "non Prime Number"
fi
