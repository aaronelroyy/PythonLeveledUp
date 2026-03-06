# itertools : product, permutations, combinations, accumulate, groupby and infinite iterators

# product
from itertools import product

a = [1, 2]
b = [3, 4]

prod = product(a, b)
print(list(prod))

c = [1, 2]
d = [3]

prod1 = product(c, d, repeat=2)
print(list(prod1))

# permutations
from itertools import permutations

p = [1, 2, 3]

perm = permutations(p, 2)
print(list(perm))

# combinations
from itertools import combinations, combinations_with_replacement

y = [1, 2, 3]

cbs = combinations(y, 2)
print(list(cbs))
cbs_wr = combinations_with_replacement(y, 2)
print(list(cbs_wr))

# accumulate
from itertools import accumulate as acs
import operator as op

ac = [1, 2, 5, 3, 4]

acc = acs(ac, func=op.mul)
print(list(acc))

acm = acs(ac, func=max)
print(list(acm))

# groupby
from itertools import groupby as gb

g = [1, 2, 3, 4]


def smaller_than(x):
    return x < 3


group_obj = gb(g, key=smaller_than)
for key, value in group_obj:
    print(key, list(value))

persons = [
    {"name": "Tim", "age": 25},
    {"name": "Dan", "age": 25},
    {"name": "Lisa", "age": 27},
    {"name": "Matt", "age": 30},
]

group_obj1 = gb(persons, key=lambda k: k["age"])

for key, value in group_obj1:
    print(key, list(value))

"""
from itertools import count, cycle, repeat

for i in count(10):
    print(i)
    for i == 5:
        break

u = [1,2,3,4]

for i in cycle(a):
    print(i)

for i in repeat(u,4):
    print(i)
"""
