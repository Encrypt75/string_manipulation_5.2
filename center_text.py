#center() add space characters at the beginning and at the end of the string to print the string at the center. 
#Create a program that do the same functionality without using center() function.

ask_text = input("Enter any text:")

#check how many character are there
char_count = len(ask_text)

#subtruct the total number of character to 99 (the middle)
num_of_spaces = 98 - char_count // 2

#print statement
print(num_of_spaces * " ", ask_text)