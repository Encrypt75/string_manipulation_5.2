#title() makes all first letter of each word in the string, capital letter. And all other letter in small case. 
#Create a program that do the same functionality without using title() function.

string_input = input("Enter any text: ")
             
for word in string_input.split():
    if word:
        result = "".join(word[0].upper() + word[1:].lower())
    else:
        print(" ")
        
print(result)