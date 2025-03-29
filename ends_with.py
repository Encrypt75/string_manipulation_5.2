#endswith() check if the string end part matches the function parameter. 
#Create a program that do the same functionality without using endswith() function.

#ask user for an input
# Take user input
#and reverse the whole list
user_string_input = input("Input name: ")
user_string_input_storage = list(user_string_input)  # Store characters 
user_string_input_storage_rev = user_string_input_storage[::-1] 

# Take another input
ends_with = input("endswith: ")
ends_with_word_storage = list(ends_with)  # Store characters 
ends_with_word_storage_rev = ends_with_word_storage[::-1]  

# Convert lists back to strings
reverse_of_text_input = "".join(user_string_input_storage_rev)  
reverse_of_end = "".join(ends_with_word_storage_rev)

# Print results
print(reverse_of_text_input)
print(reverse_of_end)