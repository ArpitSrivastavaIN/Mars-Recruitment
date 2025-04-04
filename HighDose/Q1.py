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

def obstacle_mapper(n, obstacle_ls):
    map_matrix = [[1 for i in range(n)] for j in range(n)]
    half = n // 2
    map_matrix[half][half] = "S"
    
    for obstacle in obstacle_ls:
        x, y = obstacle[0], obstacle[1]
        # map_matrix[n // 2 - obstacle[1]][n // 2 - obstacle[0]] = 0
                    
        if x == 0 and y != 0:
            map_matrix[half - y][half] = 0
        
        elif y == 0 and x != 0:
            map_matrix[half][half + x] = 0
        
        elif x > 0 and y!= 0: # 1st quad
            map_matrix[half - y][half + x] = 0

        elif x < 0 and y < 0:
            map_matrix[half - y][half + x] = 0

        elif x < 0 and y > 0:
            map_matrix[half - y][half + x] = 0
        

    return map_matrix 


file = open(os.getcwd() + "/sample.txt", "r")

data = file.read().split("\n")
matrix = [line.split() for line in data]


obstacle_ls = [] 

for obstacle in matrix:
    y_coord = int(obstacle[0]) - int(obstacle[2])
    x_coord = int(obstacle[1]) - int(obstacle[3])
    obstacle_ls.append([x_coord, y_coord])

n = max(max(abs(i[0]), abs(i[1])) for i in obstacle_ls) * 2 + 1

map_matrix = obstacle_mapper(n, obstacle_ls)

print("---MAP---\n")
for line in map_matrix:
    for position in line:
        print(position, end=" ")
    print()   

final_pt = 4
path_matrix = obstacle_mapper((final_pt * 2) + 1, obstacle_ls)
path_matrix[0][final_pt * 2] = "F"

print("\n\n ---PATH---\n\n")

for line in path_matrix:
    for position in line:
        print(position, end=" ")
    print()  

routes = []





print(obstacle_ls)