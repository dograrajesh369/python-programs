#escape sequence characters == sequence of character after backslash'\' --> escape character
'''
escape sequence of character compromise of more than one character but represent one character when 
used with in strings.
examples:- \n,(new line) \t,(tab) \',(single quotes) \\,(backslash) etc.

'''
story= "rajesh is good.\nhe is very good."
print(story)

story= "rajesh is good.\nhe\t is very good."
print(story)

story= "rajesh is good.\nhe is \very good."
print(story)