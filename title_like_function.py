#title() makes all first letter of each word in the string, capital letter. And all other letter in small case. 
#Create a program that do the same functionality without using title() function.

#ask user for an input
string_input = input("Enter any text: ")

#storage for every word            
result = []

#this fixes which one to capitalize and which are not
for word in string_input.split():
    if word:
        result.append(word[0].upper() + word[1:].lower())  

#join to convert list to string
final_result = " ".join(result)

#print statement
print(final_result)
