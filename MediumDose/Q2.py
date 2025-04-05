#EC24I1001
#Arpit Srivastava

'''
The Mars rover communicates with Earth using Morse code, 
a system where each letter and number is represented by a unique 
combination of dots (.) and dashes (-). Due to signal interference,
some messages arrive in Morse code and need to be decoded into 
readable text before mission control can understand them. Your 
task is to write a function that takes a Morse code message as 
input and deciphers it into plain english text.

'''

#Dictionary that stores the morse code for each alphabet
morse_dict = {
    ".-": "A", 
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E", 
    "..-.": "F",
    "--.": "G", 
    "....": "H", 
    "..": "I", 
    ".---": "J", 
    "-.-": "K", 
    ".-..": "L", 
    "--": "M", 
    "-.": "N", 
    "---": "O", 
    ".--.": "P", 
    "--.-": "Q", 
    ".-.": "R", 
    "...": "S", 
    "-": "T", 
    "..-": "U", 
    "...-": "V", 
    ".--": "W", 
    "-..-": "X", 
    "-.--": "Y", 
    "--..": "Z", 
    "-----": "0", 
    ".----": "1", 
    "..---": "2", 
    "...--": "3", 
    "....-": "4",
    ".....": "5", 
    "-....": "6", 
    "--...": "7", 
    "---..": "8", 
    "----.": "9"
}

#Taking User input 
morse_code_message = input("Enter Your Morse Code: ").split()

#Variable to store the decoded message
decoded_msg = ""

#For loop that iterates through the message and converts each morse code to plain text
for key in morse_code_message:
    #Appending the decoded message
    decoded_msg += morse_dict[key]

#Displaying the decoded message
print(decoded_msg)
    

