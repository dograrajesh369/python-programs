'''
Dictionary methods :-
consider the following dictionary 
a={"name" : "Rajesh" 
    "from" : "india"
    "marks" : "[85,98,99,100]}
1) a.item() : return a list of (key value) tuple
2) a.keys() : return a list containing dictionary's keys
3) a.update({"friend" : "sam"}) : updates the dictionary with suplied key - value pairs
'''
mydict= {"rajesh": 'best known as coder',
        "meenu": 'best wife',
        "nishu": 'workoholik',
        "anotherdict": {"rajesh": 'a coder',
        'marks': [1,2,3,4,5,6],
        1:2
        }}

print(list(mydict.keys())) #print key of the dictionary
print(mydict.values()) #print the values of the dictionary
print(mydict.items()) #print the (key, value) of all items of the dictionary
print(mydict)
updatedict = {
    "ravi" : "best person",
    "divya" : "friend"

}
mydict.update(updatedict) #update the dictionay by adding key- value pairs from updatedict
print(mydict)
print(mydict.get("ravi")) #return the value of the specified keys (and value is returned eg: "ravi" is returened here)
print(mydict["ravi"])

# the difference between .get and [] syntax in dictionary

print(mydict.get("ravi2")) #returns none as "ravi2" is not present in the dictionary
print(mydict["ravi2"]) #trows an error as "ravi2" is not present in the dictionary
