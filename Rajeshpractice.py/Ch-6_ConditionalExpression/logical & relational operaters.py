'''Logical operaters:-
In python logical operaters operate on conditional statements. ex:- 
and -->  true if both operands are true else false
or -->   true if atleast one operand is true else false
not -->  inverts true to false & false to true
'''

age=(int(input("enter your age")))

if(age>18 and age<50 ):
    print("you can work with us")
else:
    print("you cannot work with us")
    