# write a python function to remove a given word from a String and strip it at 
# the same time.
                                # example
# name = "   Rajesh is a good boy   "
# print(name)
# print(name.strip()) 

def remove_split(string, word):
    newstr = string.replace(word,"Anaya")
    return newstr.strip()
Name = ("Rajesh is avery rich person")
n =remove_split(Name,"Rajesh")
print(n)
