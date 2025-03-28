#lower() converts all characters of the string into lower case. 
#Create a program that do the same functionality without using lower() function.

#ask for users name or any input
user_input = input("Enter name: ")

#storage for raw characters
characters_storage = []

#appends every characters to list
for every_char in user_input:
    characters_storage.append(every_char)

#storage for converted to lower characters
new_storage = []

#checks if the character is capital or not
for every_letter in characters_storage:
    if every_letter.isupper():
        swpcs = every_letter.swapcase()
        new_storage.append(swpcs)
    else:
        new_storage.append(every_letter)

#converts list to string
lst_to_string = "".join(new_storage)

#print statement
print(lst_to_string)