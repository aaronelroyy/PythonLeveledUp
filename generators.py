# generator is executed when it is iterated through


def mygenerator():
    yield 1
    yield 4
    yield 3


g = mygenerator()


"""
value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)
"""
# print(sum(g))

print(sorted(g))
