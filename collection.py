# collections : Counter, namedtuple, orderedDict, defaultDict, deque

# Counter
from collections import Counter

a = "aaaabbbcc"
my_counter = Counter(a)
print(my_counter.items())
print(my_counter.most_common(2)[0][1])  # returns a list with tuples within
print(list(my_counter.elements()))

"""
()-> refers to number of most common items the users wants to be display
[0]-> refers to the index of the multiple tuples
[1]-> refers to the index of the element within the tuple
"""

# namedtuple
from collections import namedtuple as nt

Point = nt("Point", "x,y")
pt = Point(1, -4)
print(pt)

# deque
from collections import deque

d = deque()

d.append(1)
d.append(2)

d.appendleft(3)
d.popleft()

"""
d.extendleft can have multiple arguments enclosed in a list
d.clear
d.rotate(1) rotate tht many places to the right for left index should be negative
"""

print(d)
