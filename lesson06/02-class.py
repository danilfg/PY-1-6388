# basic class, attributes, type-annotation
class Human:
    first_name: str
    last_name: str
    hair_color: str
    eye_color: str
    age: int
    weight: float


person1 = Human()  # конструктор объекта
person2 = Human()

person1.last_name = "Doe"
person1.age = 10
person1.weight = 20.0

print(f"{person1.first_name} {person1.last_name}")
print(person2.last_name)
