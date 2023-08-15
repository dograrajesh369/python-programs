'''
sometimes we want to play pubg on our phone if the day is sunday
sometimes we order ice-cream online if the day is sunny.
sometimes we go hiking if our parents allow.

**** all these are decisions which depends on condition being met.

in python programming too, we must be able to execute instruction on a condition(s) being met. 
this is what conditionals are for !!!

If else  and elif in python 
if else and elif statements are a multiway decisions taken by our program due to certain conditions in our code.

'''

a=45
if(a<12):
    print("the value of a is smaller than 12")
elif(a>4):
    print("the value of a is greater than 4")
elif(a==12):
    print("the value of a is equal to 12")
else:
    print("a is greater than 12 and 4")

#multiple if statment

b=20
if(b<5):
    print("the value of b is smaller than 5")
if(b==5):
    print("the value of b is equal to 5")
if(b>5):
    print("the value of b is is greater than 5")
else:
    print("the value of b is not equal to 5 and smaller than 5")