# creating a empty set 
b=set()
print(type(b))

#adding value to an empty set
b.add(2)
b.add(4)
b.add(3)
b.add((3,5,6,7,8))
b.add(89)
print(b) 
b.remove(89) # remove 89 from set b
print(b)
print(len(b)) # length of the set
b.add(45)
b.pop()
print(b)