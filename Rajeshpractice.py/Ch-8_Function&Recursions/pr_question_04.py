# Write a recursive function to calculate the sum of first n natural numbers.
# n! = n*!(n-1) 
# sum(n) = sum(n-1)+n


def sum(n):
 if n==1 or n==0:  #---->>> base condition which doesn't call the function any further
    return 1
       
 else:
        return n+sum(n-1)
 
f= sum(13)
print(f)



