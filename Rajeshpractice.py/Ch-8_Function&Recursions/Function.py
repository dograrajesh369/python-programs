# program written without "Sum" function

# marks =[45,78,86,77]
# percentage = ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
# print(percentage)

# # program written with "Sum" function  using for small program

# marks1 =[85,98,96,84]
# percentage1 = (sum(marks1)/400)*100
# print(percentage1)

# using def function

def percent(marks):
    return ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100

#  or

        # p= ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
        # return p
    

marks =[85,98,96,84]
percentage = percent(marks)
print(percentage)

marks =[45,78,86,77]
percentage1 = percent(marks)
print(percentage1)


