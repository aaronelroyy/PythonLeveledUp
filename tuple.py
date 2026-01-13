# Tuple: ordered, immutable, allows duplicate elements

mytuple = ("Max", 28 , "Boston") #parentheses is optional
#single element in tuple is string u have to put comma at end

tuple_2= tuple(["max", 28, "Boston"])
print(tuple_2)

item = mytuple[-1]
print(item)

my_tuple = ['a', 'p', 'p', 'l', 'e' ]
print(my_tuple.count('p'))
print(my_tuple.index('p'))

my_list = list(my_tuple)
print(my_list)

a = (1,2,3,4,5,6,7,8,9,10)

b = a[2:5]
print(b)
c = a[2:5:2]
print(c)

my_tuple2 = "max" , 28 , "Boston"

name, age, city = my_tuple2
print(name , age , city, sep=' ')

my_tuple3 = (1,2,3,4,5,6)

i1 , *i2 , i3 = my_tuple3
print(i1, i2, i3, sep = ' ')


# sys.getsizeof tuple uses lesser bytes more efficient