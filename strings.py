# Tuple: ordered, immutable, text representation

my_string = """hello \
world"""

print(my_string)

char = my_string[-1]
print(char)

# and step index and slicing

name = "hello"
greeting = "hi"

constr = name + greeting
print(constr)

# loop: can check for substrings as well

# my_string.strip() needs to be assigned to another string bcz strings are immutable therefore can't update the current expression
"""
my_string.upper()
my_string.lower()
my_string.endswith() bool
my_string.startswith() bool
my_string.find() returns index for first found instance of the letter or substring.. return -1 if false
my_string.count() returns how many time the element exists
my_string.replace("", "")

"""
# to make a string into a list
str1 = "how are u doing"
str2 = str1.split(" ")
print(str2)
# to make a list into a string
str3 = " ".join(str2)  # or run a loop but it is more expensive wrt time
print(str3)

# f-strings

var = 1.23455
var2 = 3.43445

mystring = f"the variables are {var*2} and {var2}"
print(mystring)
