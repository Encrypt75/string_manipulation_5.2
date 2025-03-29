#endswith() check if the string end part matches the function parameter. 
#Create a program that do the same functionality without using endswith() function.

#ask user for an input
#take user input
#and reverse the whole list
user_string_input = input("Input name: ")
user_string_input_storage = list(user_string_input)  
user_string_input_storage_rev = user_string_input_storage[::-1] 

#take another input
ends_with = input("endswith: ")
ends_with_word_storage = list(ends_with)  
ends_with_word_storage_rev = ends_with_word_storage[::-1]  

#convert lists back to strings
reverse_of_text_input = "".join(user_string_input_storage_rev)  
reverse_of_end = "".join(ends_with_word_storage_rev)

#print statement
ask = reverse_of_text_input.startswith(reverse_of_end)
print(ask) 