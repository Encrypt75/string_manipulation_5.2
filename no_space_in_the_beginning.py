#lstrip() remove the space characters at the beginning of the string. 
#Create a program that do the same functionality without using lstrip() function.

#ask for string input
ask_string_input = input("Enter text/messege: ")

for every_char in ask_string_input:
    if every_char.isalpha():
        print(f"{every_char} = True")
    else: 
        print(f"{every_char} = False")

#ask user input
#for loop checking for each character
    #if char is not alphabet
        #replace(" ", "")
    #else:
        #pass