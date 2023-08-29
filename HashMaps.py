# HashMap (aka dictionary)
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77
print(myMap)    # {output 'alice': 88, 'bob': 77}
print(len(myMap))    # Output 2

myMap["alice"] = 80
print(myMap["alice"]) # Output 80

print("alice" in myMap) # Output True
myMap.pop("alice")
print("alice" in myMap) # Output False

myMap = { "alice": 90, "bob": 70 }
print(myMap) #Output { "alice": 90, "bob": 70 }