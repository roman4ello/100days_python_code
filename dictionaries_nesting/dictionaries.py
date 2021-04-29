programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

print(programming_dictionary.get("Bug"))
print(programming_dictionary["Bug"])
print(programming_dictionary)

# adding new items to dictionary
programming_dictionary["new_key"] = "some value for new_key"
print(programming_dictionary)
print(len(programming_dictionary))

# create empty dictionary
empty_dictionary = {}
print(empty_dictionary)

# wipe dictionary
# programming_dictionary ={}
# print(programming_dictionary)


# edit an item in a dictionary
print(programming_dictionary["Bug"])
programming_dictionary["Bug"] = "updated value for key 'Bug' in the dictionary"
print(programming_dictionary)

# loop through dictionary
for key in programming_dictionary:
    print(key)#print only key
    print(programming_dictionary[key]) #provide values
