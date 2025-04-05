#EC24I1001
#Arpit Srivastava

'''
'''

import os
import statistics

def average(data):
    average = 0
    for i in data:
        average += i
    
    average /= len(data)
    return average

def muchiko(data, window_size):
    data = [average([data[i + j] for j in range(window_size)]) for i in range(len(data) - window_size + 1)] 
    return data 

def sanchiko(data , window_size):
    data =  [sorted([data[i + j] for j in range(window_size)]) for i in range(len(data) - window_size + 1)]
    data = [int(statistics.median(sublist)) for sublist in data]
    return data

window_size = 3

file = open(os.getcwd() + "/log.txt", "r")

data = file.read().split()
data = [int(i) for i in data]
print(f"Unfiltered Data : {data}")

data = muchiko(data, window_size)
data = sanchiko(data, window_size)

print(f"Filtered Data :   {data}")