#isupper() check if all characters of the string is on upper case. 
#Create a program that do the same functionality without using isupper() function.

#ask user for input
user_string_input = input("Enter a string: ")

#checks if there is a small letter in the inputed string
if user_string_input.islower():
    print("False")

else:
    print("True")