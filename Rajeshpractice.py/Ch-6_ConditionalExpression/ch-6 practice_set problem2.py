#write a program to find out whether a student is pass or fail, if it requires total 40% and atleast 
#33% in each subject to pass. assume 3 subject and take mark as an input from the user.

sub1=int(input("enter 1st subject marks:\n "))
sub2=int(input("enter 2nd subject marks:\n "))
sub3=int(input("enter 3rd subject marks:\n "))
if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail because of score less than 33")
elif(sub1 + sub2 + sub3)/3<40:
    print("you are fail because you score less than 40%")
else:
    print("Congratulation!! you pass the exam")
