#ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. 
#Create a program that do the same functionality without using ljust() function.

#ask user for an input
string_input = input("Enter string_input: ")

index = 0

# Find the first letter after the space
while index < len(string_input) and string_input[index] == " ":
    index += 1

# Create the stripped string starting from the first letter
result = string_input[index:]

#print statement
print(result)  