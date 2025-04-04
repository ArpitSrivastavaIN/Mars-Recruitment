#EC24I1001
#Arpit Srivastava

'''
1)Task:
 The Rover, Brick, has a simple task — detect a Red circle marker on the ground, reach its location, and perform a 360-degree turn.

Caution: You will only get points if the center of the rover is exactly above the marker when performing the turn.

What Happened:
The camera is mounted on top of the rover at the front and top position of the rover.
Brick started from the designated starting line. After covering some distance, its camera detected the marker at coordinates (x, y, -60).
The rover navigated towards the marker and performed the 360-degree turn.
However, instead of turning at the marker, it performed the turn 55 cm behind the actual marker.
Your Task:
Write a program to adjust the rover’s navigation system so that it reaches the correct position and precisely performs the 360-degree turn on the marker.
Hint : 
Try taking a different frame of reference.
Input:
The camera’s detection coordinates (x, y, -60)
Output:
New Position (x_final, y_final, z_final) of the marker w.r.t. new frame of  reference
Write a function to get the distance between the marker and camera before and after changing the navigation reference.

'''

import math

#Function to create new frame of reference
def newFrame(x, y, offset, distance):

    new_x = round(x + (offset * (x / distance)), 2)
    new_y = round(y + (offset * (y / distance)), 2)

    return new_x, new_y

#Function to calculate distance between 2 points
def get_distance(x1, y1, z1, x2, y2, z2):

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)

#Function to calculate the distance between the marker and camera before and after change in frame of reference
def distBeforeAfter(x, y, z,new_x, new_y, offset, distance):

    #Calculating distance before change of reference
    dist_before = round(abs(get_distance(x, y, z, 0, 0, 0)))
    print(f"Distance before : {dist_before}")

    #Calculating new camer x, y coordinates wrt new frame of reference
    new_camera_x = round(offset * (x / distance), 2)
    new_camera_y = round(offset * (y / distance), 2)

    #Calculating distance after change of reference    
    dist_after = round(abs(get_distance(new_x, new_y, z, new_camera_x, new_camera_y, 0)))
    print(f"Distance after : {dist_after}")

#Taking user input for coordinates of
x, y, z = input("Enter camera's detection coordinates : ").split()
x, y, z = int(x), int(y), int(z)
offset = 55

#Calculate distance between origin and marker
distance = get_distance(x, y, 0, 0, 0, 0)

#Find New coordinates of marker
new_x, new_y = newFrame(x, y, offset, distance) 


print(f"New Position ({new_x}, {new_y}, {z})")
distBeforeAfter(x, y, z, new_x,new_y, offset, distance)
