# write a program to calculate  the grade  of a student from his marks from the following scheme:-
'''
90- 100--> EX
80-90--> A
70-80 -->B
60-70 -->C
50-60 --> D
<50 --> F
'''

marks=int(input("enter your marks : \n"))

if marks>=90:
    grade= "EX"

elif marks>=80:
    grade= "A"

elif marks>=70:
    grade= "B"

elif marks>=60:
    grade= "C"

elif marks>=50:
    grade= "D"
else:
    grade= "F"    
print("your grade is " + grade)