# A seed = the starting value that the random algorithm uses to begin generating numbers.
# reproducible values

import random as rdm

rdm.seed(1)
print(rdm.random())
print(rdm.randint(1, 10))

rdm.seed(2)
print(rdm.random())
print(rdm.randint(1, 10))

rdm.seed(1)
print(rdm.random())
print(rdm.randint(1, 10))
