'''
this function allows the user to take input from keyboard as a string.
a=input("enter your name")  ==== if a is "Rajesh" the user enter Rajesh
it is important to note that the output of input is always a string (even if the number is entered).
example :- if a is "32" user entered 32.
'''

a=input("enter your name: ")
#a=int(a) #convert a to an integer(if possible)
print(type(a))