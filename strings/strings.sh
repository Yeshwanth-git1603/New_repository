#!/usr/bin/bash


# printing a string

string="yeshwanth"
echo "$string"

#length of a string

new_str="hydrerabad"
echo "${#new_str}"

# concatination of a string

city="high"
city2="city"
city3=$city1$city2


#lower case to upper case

upper_case="hello world"
echo "${upper_case^^}"


# upper case to lower case

lower_case="hyderabad"
echo "${lower_case,,}"

#replacing the given word

word="linux cmd"
echo ${word/cmd/command}


# slicing the string

string2="python programming"

echo "${string2:1:7}"


#looping the statements

loop_str="spiderman"

for i in ${loop_str}
do
	echo "$i"
done
