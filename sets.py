# Tuple: unordered, mutable, no duplicate elements

myset = {1,2,3}
print(myset)

myset1 = set("hello")
print(myset1)

myset.add(4)
#myset.remove is not possible
myset.discard(1)
print(myset)

for i in myset:
    print(i, end = ' ')
    
print()

odds = {1,3,5,7,9}
even = {0,2,4,6,8}
prime = {2,3,5,7}

u = odds.union(even)
print(u)

i = odds.intersection(even)
print(i)

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,20,22,23}

diff1 = setB.difference(setA)
print(diff1)
diff2 = setA.difference(setB)
print(diff2)

diffs2 = setA.symmetric_difference(setB) #prints elements opposite to the elements printed during intersection
print(diffs2)

setA.update(setB)
print(setA)

setA.intersection_update(setB)
print(setA)

#same for difference_update and symmetric_difference_update

A = {1,2,3,4}
B = {1,2,3}

print(B.issubset(setA))
print(A.issuperset(setB))
print(A.isdisjoint(setB)) #intersection is an epmty set

a = frozenset([1,2,3,4])