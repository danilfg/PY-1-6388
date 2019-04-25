# Get/set attributes with wrappers
class User:
    name: str
    profile: dict

    def __init__(self, name):
        self.name = name

    # def __setattr__(self, key, value):
    #     pass

    def __getattr__(self, item):
        return self.profile[item] if self.profile.get(item) else 'Undefined'


a = User('John')
a.profile = {
    "login": 'admin',
    "password": '123123'
}
print(a.name)
print(a.password)
print(a.address)


class Debugger:
    _instance = None

    def __init__(self, instance_object):
        self._instance = instance_object

    def __getattribute__(self, item):
        print(f"Called: {item}")
        return getattr(self._instance, item)

    def __setattr__(self, key, value):
        print(f"Set: {key}, value: {value}")
        setattr(self._instance, key, value)


user = User("Artur")

debug_user = Debugger(user)

print(debug_user.name)
debug_user.name = 10
