'''
A spam comment is definded as a text containing following keywords:
"make a lot of money", "buy now", "subscribe this", "click this".
write a program to detect this spams. 
'''

text = input("enter your text : \n")

if("make a lot of money"  in text):
    spam = True
elif("buy now"  in text):
    spam = True
elif("subscribe this"  in text):
    spam = True
elif("click this"  in text):
    spam = True
else:
    spam = False
if(spam):
    print("this text is spam")
else:
    print("this is not spam")
