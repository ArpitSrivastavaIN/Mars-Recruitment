#EC24I1001
#Arpit Srivastava

'''
'''

import os

def average(data):
    average = 0
    for i in data:
        average += i
    
    average /= len(data)
    return average

def muchiko(data, window_size):
    data = [average([data[i], data[i + 1], data[i + 2]]) for i in range(len(data) - 2)] 
    print(data)       


window_size = 3

file = open(os.getcwd() + "/log.txt", "r")

data = file.read().split()
data = [int(i) for i in data]

muchiko(data, window_size)

