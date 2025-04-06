#EC24I1001
#Arpit Srivastava

'''
Given an array of sensor readings from log.txt, Write a 
code for removing the noises in the data using the Martian 
filters from the last meeting that helped the rover succeed.
Note - We are expecting you to apply different combinations of the given filter and conclude with the best - Muchiko, Sanchiko, or hybrid.
'''

import os
import statistics

#Function to calculate the average of a list
def average(data):
    average = 0
    for i in data:
        average += i
    
    average /= len(data)
    return average

#Muchiko Filter
def muchiko(data, window_size):
    data = [average([data[i + j] for j in range(window_size)]) for i in range(len(data) - window_size + 1)] 
    return data 

#Sanchiko FIlter
def sanchiko(data , window_size):
    data =  [sorted([data[i + j] for j in range(window_size)]) for i in range(len(data) - window_size + 1)]
    data = [int(statistics.median(sublist)) for sublist in data]
    return data

#Window_size so that determines how many neighbouring values will effect the readings
window_size = 3

#Reading the log.txt file
file = open(os.getcwd() + "/log.txt", "r")

#Converting the data into a list of integers
data = file.read().split()
data = [int(i) for i in data]
print(f"Unfiltered Data : {data}")

#Applying a ybrid combination of muchiko and sanchiko filter for best results.
data = muchiko(data, window_size)
data = sanchiko(data, window_size)

print(f"Filtered Data :   {data}")