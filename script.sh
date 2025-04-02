
#EC24I1001
#Arpit Srivastava

#Low Dose

#1.) Make Directory command to create a directory named "rover_mission"
mkdir rover_mission
#Changing Directory to "rover_mission"
cd rover_mission

#2.) TOuch command to create 3 empty text files
touch log1.txt
touch log2.txt
touch log3.txt

#3.)  Using mv command to rename file
mv log1.txt mission_log.txt

#4.) Using find command to find all files in the directory with .log extension
find . -name "*.log"

#5.) Cat function to display the contents of the "mission_log.txt" file
cat mission_log.txt

#6.) Grep command to find and display the word error inside "mission_log.txt"
grep "ERROR" mission_log.txt

#7.) WC command to 
wc -l mission_log.txt

#8.) Show the system's current date and time using date command
date

#9.) TOP command to dipslay the CPU usage of your system in real time
top

#10.) Scheduling a command to shut down the system in 10 minutes
sudo shutdown +10
