#lstrip() remove the space characters at the beginning of the string. 
#Create a program that do the same functionality without using lstrip() function.

#str storage
character = []

#ask for string input
ask_string_input = input("Enter text/messege: ")

#checks if every character is an alpabet
for every_char in ask_string_input:
    if every_char.isalpha():
        character.append(every_char)
    else: 
        pass

#convert list into string
lst_to_strng = " ".join(character)

#remove spaces in between the str
remove_space = lst_to_strng.replace(" ", "")

#print statement
print(remove_space)