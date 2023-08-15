# n! = 1*2*3*4.....n
# # n! = [1*2*3*4....n-1]*n
# # n! = n*(n-1)!

# # n =4
# # product = 1
# # for i in range(n):  
# #     product = product *(i+1)
# # print (product)

#                         # another way by using factorial_iter

# # def factorial_iter(n):
# #     product = 1
# #     for i in range(n):  
# #         product = product *(i+1)
# #     return product

# # f= factorial_iter(5)
# # print(f)

#                         #  using factorial_recursive formula    [n! = n*(n-1)!]

# def factorial_recursive(n):
#     if n==1 or n==0:  #---->>> base condition which doesn't call the function any further
#         return 1
#     else:
#         return n*factorial_recursive(n-1) #-->> function calling itself
    

# f= factorial_recursive(5)
# print(f)

                    # same (test instead of "factorial_recursive" try with "i")

def i(n):
    if n==1 or n==0:
        return 1
    else:
        return n*i(n-1)
    

f= i(5)
print("The n natural number: ",f)