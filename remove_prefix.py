#removeprefix() remove the characters at the beginning of the string that matches the function parameter. 
#Create a program that do the same functionality without using removeprefix() function.

#ask user for an input
user_string_input = input("Input name: ")

#ask user what to remove
string_remover = input("remove prefix: ")

if user_string_input.startswith(string_remover):
    remove = user_string_input.replace(string_remover, "")

else:
    pass

print(remove)