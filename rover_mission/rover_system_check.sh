#!/bin/bash

var=$(( RANDOM % 100))
echo "Battery Percentage : $var "

if [[ $var -lt 20 ]]; then
	echo "Battery percentage less than 20%"
	echo "[LOG] : Battery low! Return to base!" >> mission_log.txt
	exit 1
fi

check=$(ping -c 1 google.com > /dev/null 2>&1; echo $?)

if [ $check -eq 0 ]
then
	echo "Host Reachable"
	echo "[LOG] : All systems Operational!" >> mission_log.txt
else
	echo "[LOG] : Communication Failure!" >> mission_log.txt
	echo "Host Unreachable"
fi
