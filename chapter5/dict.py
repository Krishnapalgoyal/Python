 # list of key value pairs 
# it is inorders
# it is mutable
#it is indexed
# Can not contain duplicates keys 
d = {} # emty dectionory 
marks = {
    "Krishnapal" : 100, 
    "jugal": 89,
    "rohit": 23
}

print(marks, type(marks))
print(marks["Krishnapal"])

print(marks.get("Krishnapal"))
print(marks.get("test")) # it will give none if the key is not exist 
print(marks["test"]) # it give a key error if key is not exist 


