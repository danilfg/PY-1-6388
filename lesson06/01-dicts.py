# complex structure
person1 = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "hair_color": "Green",
    "eyes_color": "Brown",
    "weight": 95.4
}
person2 = {
    "first_name": "Artur",
    "last_name": "Doe",
    "age": 45,
    "hair_color": "Green",
    "eyes_color": "Brown",
    "weight": 75.4
}


def get_full_name(person: dict):
    return f"{person['first_name']} {person['last_name']}"


def show_info(person: dict):
    print("Person:", get_full_name(person), "age: ")


def show_all_persons_info(persons: list):
    for x in persons:
        show_info(x)


# function to work with it
show_info(person1)
show_info(person2)

# work with dict global list
person_list = [person1, person2]

show_all_persons_info(person_list)
