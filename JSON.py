"""
dict-> object,
list,tuple -> array,
str-> string,
int, long, float -> number
True -> true
False -> false
None -> null
"""

import json

# from Python to JSON (serialization/encoding)
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "tilles": ["programmer", "engineering student"],
}

personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

"""
with open ('person.json', 'w') as file:
    json.dump(person, file, indent =4)"""

# from JSON to Python (deserialization/decoding)

with open("person.json", "r") as file:
    person = json.load(file)
    print(person)
