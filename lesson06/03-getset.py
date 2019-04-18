# property (get/set), encapsulation
class Human:
    first_name: str = 'John'
    last_name: str = 'Doe'
    hair_color: str
    eye_color: str
    __age: int = 200  # private
    weight: float

    @property  # getter => fullname() -> fullname
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 0 < value < 120:
            self.__age = value
        else:
            print('Invalid age value')


person1 = Human()
# person1.first_name
# print(person1.fullname)
# person1.age = -100
# print(person1.age)
# person1.age = 100
# person1.set_age(-100)
# print(person1._Human__age)

