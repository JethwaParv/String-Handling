# Task 12 string handling
print('======================Alternate character uppercase=======================')
# Using loop for string handling
# This task makes every alternative character in the sentence below upper case and the remainder lower.
string = str(input('Enter a string:\n'))
final_string = ''
for i in range(len(string)):
    if i % 2 == 1:  # Modulo operator(%) to check if it is an even or odd index.
        final_string += string[i].upper()
    else:   # The else statement handles index that is not upper case, but is lower case.
        final_string += string[i].lower()
        print(final_string)

print('=================Alternate word capital==============================')
split_string = string.split()                         #to store the split string -creates a list

final_string = ""                                     #to compile the resulting string

for i in range(len(split_string)):                      #for loop for repeat operation

    if i % 2 == 0:
        final_string += split_string[i].upper() + " "   #if item index divides by 2 then convert to uppercase

    else:
        final_string += split_string[i].lower() + " "   #otherwise convert to lowercase

print(final_string)
