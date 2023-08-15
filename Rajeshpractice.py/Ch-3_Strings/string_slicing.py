#a string in python can be sliced for getting a part of the string.
#consider  the following string:-
#name = "Rajesh"  => lenght =6
#        012345
#      -6-5-4-3-2-1
# The index in a string start from 0 to(length-1) in python. In order to slice a string, 
# we use the following syntax.         

greeting="Good Morning, "
name = "Rajesh"

#concatenating two strings
a=(greeting+name)
print(a)                        

#second way to print
a=(greeting)
b=(name)
print(a+b)
print(type(name))

#string slicing
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[0:3])
print(name[1:5])
print(name[:5])
print(name[0:])  

