# write a program to print 1 to 50 using a while loop.

# i = 1
# while i<=50:
#     print(i)
# i = i+1


# i = 0
# while i<5:
#     print("rajesh " + str(i))
#     i = i+1


n=int(input("Enter number:"))
a = 0
b = 1
if n < 0: 
    print("Incorrect input") 
elif n == 0: 
    print(a)
elif n == 1: 
    print(b) 
else: 
    for i in range(2,n): 
        c = a + b 
        a = b 
        b = c 
    print(b)




    