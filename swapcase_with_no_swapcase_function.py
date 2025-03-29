#ask user for an input
enter_name = input("Enter you name: ")

#storage for string
string_storage = []

#decide what to do for every string
for letter in enter_name:
    if letter.islower():
        upsize = letter.upper()
        string_storage.append(upsize)

    else:
        downsize = letter.lower()
        string_storage.append(downsize)

#print statement and joins the list to convert it back to a string
print("".join(string_storage))