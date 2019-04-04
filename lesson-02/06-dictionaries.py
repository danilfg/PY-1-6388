# key-value pairs, methods, usage example
user = ["John", "Doe", "Developer", 30, "Moscow"]

print(user[2])

user_dict = {
    "name": "John",
    "surname": "Doe",
    "role": "Developer",
    "age": 30,
    "city": "Moscow"
}

print(user_dict["name"])

for key, value in user_dict.items():
    print(f"Key {key} is {value}")
