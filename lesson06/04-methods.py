# object functions, arguments
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

    def walk(self, steps: int) -> None:
        for x in range(steps):
            print(f"Person {self.first_name}: walking ... {x} ...")

    def sleep(self, seconds: int):
        pass

    def say(self, message: str):
        print(f"{self.first_name}: {message}")


person1 = Human()
person2 = Human()
person1.walk(10)
person2.walk(10)

person2.say("Hello world!")
