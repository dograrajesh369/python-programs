#String function == some of the mostly used function to perform operations on or manipulate strings are:-


story= '''once upon a time there was a hotiler name called "Rajesh" start learning python program and 
become champion on that 
and start earning very good package.
'''
print(story[0:25])

#string functions:-
#len()function == this function returns the length of the strings.

print(len(story))
'''
string endswith== this function tells whether the variable string ends with string "age" or not 
if string is "age", it returns true for "age" since "package" ends with age, else it will return false
'''
print(story.endswith("\n"))   

#string.count("c") == count the total number of occurance of any character
print(story.count("a"))

#string.capitalize() == this function capitalizes the first character of a given string
print(story.capitalize())
'''
string.find(word) == this function find a words and retuns the index of first occurance 
of that word in the string.
'''
print(story.find("package"))
'''
string.replace(oldword,newword) == this function replace the oldword with newword 
in entire string.
''' 
print(story.replace("champion","master"))
