#lstrip() remove the space characters at the beginning of the string. 
#Create a program that do the same functionality without using lstrip() function.

#str storage
character = []

#ask for string input
ask_string_input = input("Enter text/messege: ")

for every_char in ask_string_input:
    if every_char.isalpha():
        character.append(every_char)
    else: 
        pass

print(character)