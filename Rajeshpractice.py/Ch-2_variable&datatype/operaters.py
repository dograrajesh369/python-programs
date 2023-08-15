'''
following are some common operaters in python
1) arithmetic operaters = +,-,*,/ etc.
2) assignment operaters = =,+=,-=, etc.
3) comparison operaters = ==,>,>=,<,!= etc.
4) logical operaters = and,or,not
'''
#operands
# example of arithmetic operater

a=3
b=4
print("the value of a+b is:", a+b)  
print("the value of a-b is:", a-b)
print("the value of a/b is:", a/b)
print("the value of a*b is:", a*b)

# second process of print
print(f"the value of {a+b}")

#example of assignment operater
e=23 
e/=6
b=20
#b+=2
b=(b+2)
c=4  
c-=3
d=5  
d*=4

print(f'{e}\n{b}\n{c}\n{d}')

#comparison operators 
b=(6>7)
print(b)
c=(7==7)
print(c)
d=(67!=87)
print(d)    

#logical operater
bool1=True
bool2=False
print("the valve of bool1 and bool2: ", (bool1 and bool2))
print("the valve of bool1 or bool2: ", (bool1 or bool2))
print("the valve of bool1 not bool2: ", (not bool2))