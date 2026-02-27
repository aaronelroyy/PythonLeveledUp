def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(sum(firstn(10)))


def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


fib = fibonacci(5)
print(next(fib))
print(next(fib))

# my_generator = (i for i in range(10000) if i%2==0)
