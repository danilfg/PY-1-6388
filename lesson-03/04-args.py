# default values, multiple, unpack values
def hello(name="Guest"):
    print(f"Hello, {name}", "123", "#")


# hello("John")
# hello()
# hello("Guest 1")

def multiple_hello(*names, word="Hello"):
    for name in names:
        print(f"{word}, {name}")


# multiple_hello(['John', 'Artur', 'Lucy', 'Itan'])
multiple_hello('John', 'Artur', 'Lucy', 'Itan', word="Hey")
