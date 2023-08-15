
#write a program to fill in a letter template given below with name and date.

letter ='''Dear <|name|>,
Greeting of the day

you are selected!
thanx and regards
rdx
date:<|date|>
'''
name=input("enter your name \n")
date=input("enter date \n")
letter=letter.replace("<|name|>", name)
letter=letter.replace("<|date|>",date)
print(letter)