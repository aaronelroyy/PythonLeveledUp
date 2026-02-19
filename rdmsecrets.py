import secrets as sc

print(sc.randbelow(10))
print(sc.randbits(5))  # returns a 5-bit number

mylist = list("abcdef")
print(sc.choice(mylist))
