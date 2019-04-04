# code-style PEP8 (https://pep8.ru/doc/pep8/)

userInput = 10  # error
user_input = 10

# PascalCase -> class
# camelCase -> unique (not python)
# snake_case (python)

# conditions (if-else, &&, ||, <>)
age = 26
agree = False

if age < 18 and agree is not False:
    print("Error")  # else if
elif age < 18 and agree is True:
    print("Restricted")
else:
    print("Success")

# loops (for, while)
a = 0

while a < 10:
    print(a)
    a += 1

for x in range(0, 10):
    print(x)
