#EC24I1001
#Arpit Srivastava

'''
After 1,499 days on Mars, NASA's Perseverance Rover met two aliens named Muchiko and Sanchiko. They were very friendly and helpful throughout the exploration. As a gesture of friendship, NASA decided to send a gift on the next mission on April 4th — and they chose our Rover, Brick! 🎉
So, We (MaRSians) had the lucky chance to talk with the Martian People. During our chat with Muchiko, we learned that Martians use a four-number system to represent 3D rotations, unlike our three-number system. Their system is better because it avoids Gimbal lock.
To help Brick fit in, we need to create a conversion code that will translate our system into theirs.
Can you write it before the launch?.
'''

import math

def _3dto4d(x, y, z):

    #Converting to radians 
    x, y, z = math.radians(x), math.radians(y), math.radians(z)

    #Compute the half angle trigonometric values of x, y, z
    cx = math.cos(0.5 * x)
    sx = math.sin(0.5 * x)
    cy = math.cos(0.5 * y)
    sy = math.sin(0.5 * y)
    cz = math.cos(0.5 * z)
    sz = math.sin(0.5 * z)

    #Calculating the values of the Quaternion coordinates
    w4 = round(cx * cy * cz + sx * sy * sz, 5) #Scalar
    x4 = round(sx * cy * cz - cx * sy * sz, 5) #i component
    y4 = round(cx * sy * cz + sx * cy * sz, 5) #j component
    z4 = round(cx * cy * sz - sx * sy * cz, 5) #k component

    return w4, x4, y4, z4


#User input for Euler angles
x, y, z = input("Enter your Euler's angles : ").split()
x, y, z = int(x), int(y), int(z)

#Converting to QQuaternion and displaying the result
w4, x4, y4, z4 = _3dto4d(x, y, z)
print(f"Quaternion Values : {w4} + {x4}i + {y4}j + {z4}k")


