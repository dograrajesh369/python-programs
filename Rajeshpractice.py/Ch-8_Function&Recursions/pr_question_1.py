# Write a program using function to find greatest of three number.

def max(n1,n2,n3):
    if (n1>n2):
        if(n1>3):
            return n1
        else:
            return n3
    else:
        if(n2>n3):
            return n2
        else:
            return n3
        
m = max(578,98,145)
print("The value of max is: "+str(m))