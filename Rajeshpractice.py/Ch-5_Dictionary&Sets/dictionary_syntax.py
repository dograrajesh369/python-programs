#dictionary is a collection of key value pairs:
'''
syntax : 
    a={"key" : "value"
       "harry" : "code",
       "marks" : "100"
       "list" :[1,2,3,4]}

a["key"]=> print"value"
 ["list"]=> print[1,2,3,4]

 properties of a python dictionary
1) it is unordered
2) it is mutable
3) it is indexed
4) cannot contain duplicate keys

'''

mydict= {"rajesh": 'best known as coder',
        "meenu": 'best wife',
        "nishu": 'workoholik',
        "anotherdict": {"rajesh": 'a coder',
        'marks': [1,2,3,4,5,6],
        }}
print(mydict['rajesh'])
print(mydict['anotherdict']['rajesh'])
