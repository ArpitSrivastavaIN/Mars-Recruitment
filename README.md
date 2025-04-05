


# Mars Task#1

## Light Dose:
### 1. Ubuntu Terminal Commands : 
- mkdir : Commands used to create a new directory 'mkdir <*filename*>.
- cd <*path*> : Navigating into a directory.
- touch <*filename*> : Creates a file in the current working directory with filename.
- mv <*filename1*> <*filename2*> : Renaming filename1 to filename2.
- find . --name "*.log" : Find command to look for a file that has a log extension.
- cat <*filename*> : Display the contents of a file in the terminal itself.
- grep "WORD" <*filename*> : GREP command searches for WORD inside the filename.
- wc -l <*filename*> : Command to count the number of lines in a text file.
- date : Command that shows the system's current date and time.
- top : Command that displays the CPU usage and list of all processes running on the computer.
- sudo shutdown +10 : Command that will shutdown the computer after 10 minutes. Sudo is needed to get administrative privileges and +10 indicates the timer for the shutdown
#### Sources : 
- [Ubuntu Commands Cheatsheet](https://www.geeksforgeeks.org/linux-commands-cheat-sheet/)
- [Display Lines in a FIle](https://askubuntu.com/questions/442914/calculating-the-number-of-lines-in-a-file)
-  [Schedule Shutdown](https://www.geeksforgeeks.org/shutdown-command-in-linux-with-examples/)
### 2.  Bash Scripting:
#####  Learning Experience :
- chmod +x *script.sh*  : Add execution permissions to the file so as to directly execute as ./script.sh
- Learning how to use variables in bash 
- Learning how to generate a 2 digit random integer using RANDOM in bash
- `var=$(( RANDOM  %  100))`
- Using `echo` statement to output messages onto the terminal.
- Using IF code blocks in bash
- Generating a ping in bash that doesn't output anything instead stores the result in a variable which is then run through a if code block to check and log if the host was reachable.

#### Sources:
-[Generate Random 2 digit integer](https://coderwall.com/p/s2ttyg/random-number-generator-in-bash)
-[IF code blocks in bash](https://devhints.io/bash#conditionals)
-[Storing ping output in variable](https://stackoverflow.com/questions/45117591/taking-output-from-command-in-bash)

## Medium Dose:

 ### 1. Marker Location Frame:
#### Logic:
- Z coordinate of the marker indicates that the camera is at a height of 60 cm from the ground
- The rover rotates at 55 cm before the marker, which means that on the line connecting the starting point of the rover and the marker it rotates 55 cm before the marker. On this very line the new frame must be created so as to get the rover to precisely rotate around the marker. 

### 2. Morse Code Decryption:
#### Logic:
- A dictionary is used to store the Morse code for each alphabet as key and the corresponding alphabet as value to the key
-  The user input is converted into a list of alphabets and then matched with the dictionary to decode the message to plain English text.
### 3. Alphabet Position Decryption:
#### Logic:
- A dictionary is first generated with keys from 0 to 25 that stores all uppercase alphabets
- -User input is shifted by shifting the key to find the decoded alphabet.
- `Equation : new_key = (key - iter - 1) % 26`

	- Here `% 26` is there so that the key loops around the dictionary
	- iter - 1 to `shift according to its position

### 4. Noise Reduction :
#### Login:
- In a sensor data reading has large and small peaks that result in an uneven graph. To fix this we first apply the Sanchiko filter that removes or reduces the noise in the graph by remove the large peaks and the Muchiko filter is used the remove the small peaks based on neighbouring values by applying average on the data neighbouring that reading. However the window size can be altered based on the data size so as to keep the resolution of the sensor reading and ensure a smooth dataset to be used.
#### Source:
- [Filtering Sensor data](https://www.youtube.com/watch?v=4VNySdwTW_w)
### 5.   Quaternion System :
#### Logic : 

## High Dose:
### 1.  Guide Rover Brick:
#### Logic:
-  Obstacles will be converted to coordinates so as to easily map them the North direction and South direction will affect the y coordinates and the East and West will decide the x coordinate. 
- A matrix size must be decided by finding the largest individual coordinate x or y and bee multiplied by 2 and 1 added to it
- -Mapping obstacles on a 2d matrix in python is tough because the origin isn't at `map[0][0]` instead at `map[n, n]` where n is the maximum coordinate
- - With this logic we iterate through the obstacle_ls and change the value of safe positions i.e 1 to 0 which represents obstacle. For better viewing the map the origin has been set to S
#### Path finding : 

### 3. Behaviour Tree:
- File attached as pdf inside high dose.

## Maze Rover Experience :
### What i learnt? : 
- Understanding how the rover uses onboard sensor to detect the walls in the maze so that it can maneuver through the maze while applying the simplest route. We learnt how the rover deals with different scenarios within the maze how it deals with intersections, dead end and straight paths. Like for a in intersection it will calculate which path is the longest turn in the direction and move towards it. At a dead end the rover gets reading that at all three direction front, left and right the distance from the wall is the same that means that it is at a dead end and must take a 180 degree u-turn and go back. At a straight path it must continuously keep checking its left and right sensor reading for an intersection if it encounters an intersection it stops and then analyses the intersection to act accordingly. We also understand how the rover must align it self to that it is at the middle of the walls for accurate execution of path-finding to reach the Red Gate.
- Solving the maze was really fun. Spamming the speed increase button and then try-harding the direction keys helped us to solve it within 6 minutes. We also learnt about creating an executable using bash and how the sensors and the motor of the rover interact with each other. How we create a subscription to the camera to access its feed to get sensor reading and publish that data using a publisher. 

