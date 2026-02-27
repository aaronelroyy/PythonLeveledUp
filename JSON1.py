# json.dumps() only works with JSON-serializable data types, so convert custom objects → dict first.

import json


class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("max", 27)


def encode_user(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of type user is not JSON serializable")


userJSON = json.dumps(
    user, default=encode_user
)  # ``default(obj)`` is a function that should return a serializable version of obj or raise TypeError.
print(userJSON)
