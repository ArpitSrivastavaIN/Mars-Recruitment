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
Create a map of the arena using an n x n matrix.


Represent obstacles using 0 and safe positions using 1.


Print the entire arena as a matrix.


Bonus Task - Shortest Path:
Calculate the shortest path for Brick to reach the destination[10,10] from the position [0,0] while avoiding obstacles.
Good Luck, Future MaRsians! The Arena awaits your command!
'''

import os

# Obstacle reader reads the text file calculates the location of the obstacle and stores it in coordinates form in a list
def obstacle_reader():
    
    file = open(os.getcwd() + "/sample.txt", "r")

    data = file.read().split("\n")
    matrix = [line.split() for line in data]

    obstacle_ls = [] 

    #Iterating through each obstacle to find its coordinates
    for obstacle in matrix:
        if len(obstacle) >= 4:
            y_coord = int(obstacle[0]) - int(obstacle[2])
            x_coord = int(obstacle[1]) - int(obstacle[3])
            obstacle_ls.append([x_coord, y_coord])
        else:
            print("Invalid Coordinate Ignored.")

    return obstacle_ls        


# Obstacle Mapper iterates through the obstacle_ls and maps out all the obstacles

def coord_mapper(n, obstacle_ls, value):
    map_matrix = [[1 for i in range(n)] for j in range(n)]
    half = n // 2
    map_matrix[half][half] = "S"
    
    for obstacle in obstacle_ls:
        x, y = obstacle[0], obstacle[1]
                    
        if x == 0 and y != 0:
            map_matrix[half - y][half] = value
        
        elif y == 0 and x != 0:
            map_matrix[half][half + x] = value
        
        elif x > 0 and y!= 0: # 1st quad
            map_matrix[half - y][half + x] = value

        elif x < 0 and y < 0:
            map_matrix[half - y][half + x] = value

        elif x < 0 and y > 0:
            map_matrix[half - y][half + x] = value
        

    return map_matrix 

# def search(n, obstacle_ls, start=[0, 0], goal=[10, 10]):
#     n = n // 2 + 1
#     print(goal)
#     stack = [[start, [start]]]
#     path_ls, visited = [], []

#     while stack:
#         [x, y], path = stack.pop()
#         print(x, y, path)
#         if x == goal[0] and y == goal[1]:
#             path_ls.append(path) 
#             print("[GOAL reached]")
#         if [x, y] in visited or [x, y] in obstacle_ls:
#             print("Obstacle or visited block encountered")
#             continue

#         visited.append([x, y])
#         print("New block visited")
#         movement_ls = [[1, 0], [0, 1], [-1, 0], [0, -1]]

#         for dx, dy in movement_ls:
#             nx, ny = x + dx, y + dy

#             if 0 <= nx <= goal[0] and 0 <= ny <= goal[1]:
#                 stack.append([[nx, ny], path + [[nx, ny]]])
#                 print("New node appended")

#     for i in path_ls:
#         print(i)


#Reading all the obstacles and storing it in a list
obstacle_ls = obstacle_reader()

#Calculating the size of the matrix
n = max(max(abs(i[0]), abs(i[1])) for i in obstacle_ls) * 2 + 1

#Generating the matrix
map_matrix = coord_mapper(n, obstacle_ls, 0)

#Displaying the matrix
print("---MAP---\n")
for line in map_matrix:
    for position in line:
        print(position, end=" ")
    print()   

# final_pt = 10
# path_matrix = coord_mapper((final_pt * 2) + 1, obstacle_ls, 0)
# path_matrix[0][final_pt * 2] = "F"

# print("\n\n ---PATH---\n")

# for line in path_matrix:
#     for position in line:
#         print(position, end=" ")
#     print()  


# print(obstacle_ls)
# task = 0
# print(n)
# path = search(n, obstacle_ls, goal = (4, 4))
# print(path)

# if path:
#     print("Shortest Path Found:")
#     for step in path:
#         print(step)
# else:
#     print("No Path Found")