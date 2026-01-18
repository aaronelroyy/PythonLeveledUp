# Dictionary: unordered, mutable, key-value pairs

mydict = {"name": "Max", "age": 38, "City": "Kansas"}

mydict2 = dict(name="mary", age=27, City="kansas")
print(mydict2)

"""
del mydict["name"]
mydict.popitem()
"""
# by default dictionary returns key

for value in mydict.values():  # mydict.keys()
    print(value)

for key, value in mydict.items():
    print(key, value)

mydict3 = dict(mydict)
print(mydict3)

# merging dictionay
mydict.update(mydict2)
print(mydict)


numberDict = {3: 9, 6: 36, 9: 81}
print(numberDict[3])

mytuple = (8, 7)
mydict = {mytuple: 15}
print(mydict)

# not possible for list bcz it is mutable
