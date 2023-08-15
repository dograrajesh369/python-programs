#write a program to accept marks of 6 students and display them in a sorted manner

m1=int(input("entre the 1st student marks: \n"))
m2=int(input("entre the 2nd student marks: \n"))
m3=int(input("entre the 3rd student marks: \n"))
m4=int(input("entre the 4th student marks: \n"))
m5=int(input("entre the 5th student marks: \n"))
m6=int(input("entre the 6th student marks: \n"))

studentsmarks=[m1,m2,m3,m4,m5,m6]
studentsmarks.sort()    
print(studentsmarks)
