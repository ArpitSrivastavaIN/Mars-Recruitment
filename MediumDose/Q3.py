#EC24I1001
#Arpit Srivastava

'''
The Mars rover transmits encrypted messages to Earth using a special encoding method. Your task is to decode the message by reversing this pattern. (The input will contain only alphabets. If any letters are in lowercase, convert them to uppercase. The final output should always be in all caps.)
        Sample Input:'NCUW'
'N' was shifted by 1, so original = 'M'
'C' was shifted by 2, so original = 'A'
'U' was shifted by 3, so original = 'R'
'W' was shifted by 4, so original = 'S'
Sample Output:'MARS'
'''

#Creating a dictionary to store the numeric value of alphabets starting with A at 0
alphabet_dict = {i : chr(i + 65) for i in range(26)}

#Taking user input of the encrypted message converting lovercase to uppercase and forming a list
message_list = list(input("Enter the encrypted message: ").upper())

#For loop that iterates till the number of alphabets in message_list
print("Decoded Message : ", end="")
for i in range(len(message_list)):
    #Iterating through the dictionary
    for key, value in alphabet_dict.items():
        #Finding the corresponding value to user input
        if(value == message_list[i]):
            #Applying encryption
            print(alphabet_dict[(key - i - 1) % 26], end = "")
print()