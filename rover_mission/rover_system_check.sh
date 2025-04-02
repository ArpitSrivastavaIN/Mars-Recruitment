#!/bin/bash

#Creating a variable var to store the random 2 digit integer
var=$(( RANDOM % 100))

#Output the battery percentage
echo "Battery Percentage : $var "

#If block to check it the battery store in var is less than 20 
if [[ $var -lt 20 ]]; then
	echo "Battery percentage less than 20%"
	#If battery is less log into mission_log.txt that rover must return to base
	echo "[LOG] : Battery low! Return to base!" >> mission_log.txt
	exit 1
fi

#Creating a variable check to capture the ping output to google.com
check=$(ping -c 1 google.com > /dev/null 2>&1; echo $?)

#If code block to check if ping was successful if check = 0 then ping worked fine else some error.
if [ $check -eq 0 ]
then
	echo "Host Reachable"
	#Log into file that all systems operational
	echo "[LOG] : All systems Operational!" >> mission_log.txt
else
	#Log into file communication failure.
	echo "[ERROR] : Communication Failure!" >> mission_log.txt
	echo "Host Unreachable"
fi
