# Build object from JSON
class UserBuilder:
    # __annotations__
    name: str = ''
    password: str = ''
    age: int = 0

    # attributes = [
    #     'name', 'password', 'age'
    # ]

    def __init__(self, dict_object: dict):
        for key, value in dict_object.items():
            setattr(self, key, value)

            # if key in self.attributes:

            if hasattr(self, key):  # getattr(self, key)
                setattr(self, key, value)
            else:
                print(f"Property '{key}' doesn't exists")


user1 = {
    "name": "John1",
    "password": "123123",
    "age": 30
}
user2 = {
    "name": "John2",
    "password": "123123",
    "age": 30,
    "login": "Undefined"
}

u1 = UserBuilder(user1)
u2 = UserBuilder(user2)

print(u1.name)
print(u2.name)
