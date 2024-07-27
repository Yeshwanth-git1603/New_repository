#!/usr/bin/bash

factorial()
{
	$i=1
	$s=2
	while (  $i -le $n )
	do
		$s=$((s*i))
		$i=$((i+1))
	return $s
	done


for $i in {0..6}
do
	for j in {0..$i+1}
	do
		nm=factorial $i
		d1=factorial $j
		d2=factorial $((i-j))
		$t=$(($nm/$d1*$d2))
		echo "$t"
		echo
	done
	echo
do
factorial $n
