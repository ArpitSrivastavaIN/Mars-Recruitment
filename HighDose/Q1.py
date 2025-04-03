#EC24I1001
#Arpit Srivastava

'''
1)Task: Your mission is to guide  Rover Brick — the King of the Arena —  to its final destination while avoiding obstacles.
A .txt file will be provided, containing the positions of the obstacles. 
Each row represents one obstacle and Columns represent the position
1st Column: North direction


2nd Column: East direction


3rd Column: South direction


4th Column: West direction


Example - sample.txt file 
2 3 0 3
5 1 0 2
3 0 4 4
3 4 0 2
Distances have been given from the initial position.
Movement Rule:
Brick moves like a King in Chess — it can move one meter in any direction (North, South, East, West). Due to Some issues with the motor driver, Brick can’t move diagonally.
Map Creation:
Create a map of the arena using an n × n matrix.


Represent obstacles using 0 and safe positions using 1.


Print the entire arena as a matrix.


Bonus Task - Shortest Path:
Calculate the shortest path for Brick to reach the destination[10,10] from the position [0,0] while avoiding obstacles.
Good Luck, Future MaRsians! The Arena awaits your command!
'''

import os

file = open(os.getcwd() + "/sample.txt", "r")

data = file.read().split("\n")
matrix = [line.split() for line in data]


obstacle_ls = []


for obstacle in matrix:
    y_coord = int(obstacle[0]) - int(obstacle[2])
    x_coord = int(obstacle[1]) - int(obstacle[3])
    obstacle_ls.append([x_coord, y_coord])

n = max(max(i[0], i[1]) for i in obstacle_ls) * 2 + 1

map_matrix = [[0 for i in range(n)] for j in range(n)]

map_matrix[n // 2 - 0][n // 2 - 0] = "A"

for obstacle in obstacle_ls:
    map_matrix[n // 2 - obstacle[1]][n // 2 - obstacle[0]] = "1"

for line in map_matrix:
    for position in line:
        print(position, end=" ")
    print()     
