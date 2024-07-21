#!/usr/bin/bash

# associative arrays

declare -A myarray1

myarray1["name"]="yeshwanth"
myarray1["age"]=23
myarray1["city"]="hyderabad"

echo "${myarray1[@]}"


for i in ${myarray1[@]}
do
	echo "the values of array are${myarray1[@]}"
done


# noraml integer arrays


array1=(1 2 3 4 5)
echo "${array1[@]}"


array1=(1 2 3 4 5)
echo "${#array1[@]}"


array1=(1 2 3 4 5)
echo "${!array1[@]}"












