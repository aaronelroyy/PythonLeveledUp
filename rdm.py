import random

print(random.random())

print(random.uniform(1, 10))

print(random.randint(1, 10))
print(random.randrange(1, 10))  # upperbound not included

print(random.normalvariate(0, 1))

mylist = list("abcdef")

print(random.choice(mylist))
print(
    random.sample(mylist, 3)
)  # if elementrepeated in the container then two characters can be chosen
print(random.shuffle(mylist))
