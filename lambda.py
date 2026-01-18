add10 = lambda x: x + 10  # same as a defined function returning sumthign
print(add10(5))

mult = lambda x, y: x * y
print(mult(9, 9))

points2D = [(1, 2), (3, -1), (9, 9), (7, 5)]
points2D_sorted = sorted(points2D, key=lambda k: k[0] + k[1])
print(points2D_sorted)

# map(func, iterable)

a = [1, 2, 3, 4]
b = map(lambda k: k * 2, a)
print(list(b))  # print(*b)

# u can also use list comprehensions

# filter(func, iterable)

c = [1, 2, 3, 4]
d = filter(lambda k: k % 2 == 0, c)  # [x for x in a if x%2==0]
print(*d)

# reduce(func, iterable)
from functools import reduce

f = [1, 2, 3, 4, 5]

product_f = reduce(lambda x, y: x * y, f)
print(product_f)
