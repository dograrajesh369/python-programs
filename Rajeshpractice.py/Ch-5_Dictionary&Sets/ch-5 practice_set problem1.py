# write a program to create a dictionary of hindi words with values as their english translation.
#provide  user with an option  to look it up!!

mydict={
                "pankha" : "fan",
                "dabba" : "box",
                "chibb" : "dent",
                "gardi" : "car"
}

print("These are some options: ", mydict.keys())
a=input("Enter The Hindi word:- ")
#print("The Meaning of this word is: ",mydict[a])

#Below line will not throw an error if the key is not present in the dictionary
print("The Meaning of this word is:- ",mydict.get(a))

