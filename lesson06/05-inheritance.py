# multiple class usage, polymorphism, overloading
class Animal:
    name: str

    # def __init__(self, animal_name: str):
    #     self.name = animal_name

    def move(self):
        pass


class Bird(Animal):
    name = 'Bird'

    def move(self):
        self.fly()

    def fly(self):
        pass


class Cat(Animal):
    name = 'Cat'

    # def __init__(self):
    #     super().__init__('Cat')

    def move(self):
        self.walk()

    def walk(self):
        pass


cat = Cat()
birdy = Bird()
print(cat.name)
# polymorphism
cat.move()
birdy.move()
