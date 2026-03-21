# lists: ordered, mutable, allows duplicate elements
mylist = ["banana", "cherry", 1, True]

item3 = mylist[-3]
item2 = mylist[-2]
print(item3, item2, sep=" ")

mylist.append("lemon")
mylist.append("grapes")
mylist.insert(1, "blueberry")
print(mylist)

item = mylist.pop()  # last item is popped
print(item)
print(mylist)

rmelement = mylist.remove("cherry")
print(mylist)

"""
.clear()
.reverse()
.sort()
"""
list1 = [0] * 5

print(mylist)

list2 = [1, 2, 3, 4, 5]

new_list = list1 + list2
print(new_list)


list3 = [1, 2, 3, 4, 5, 6, 7, 8]

a = list3[1:6]
print(a)

"""
a = mylist[::2] every second item
a = mylist[::-2] every second item but reverse fashion
"""

list_org = ["banana", "cherry", "apple"]

list_cpy = list_org  # refer to same list in memory

# modifying copy results in modification in original

"""
=list_org.copy() 
=import copy copy.copy(__) copy.deepcopy
=list(list_org)
=list_org[:]
"""

def local(a_list):
    a_list += [200,300,400]
    a_list.append(-4)
    a_list.insert(2,"a")

o_list = [10,77,-5,4]
local(o_list)
print(o_list)
