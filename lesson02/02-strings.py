# len, slices, concat, methods, search, format (old / new)
name = "John Doe"

name_length = len(name)  # <int>

# if name_length < 10:
#     error

print(name[0:4])
print(name[5:])
print(name[0:5:2])
print(name[::-1])

full_name = "John" + " " + "Doe"

print(name.find(' '))


first = "Python"
second = "a language"

print("{} is {}".format(first, second))
print(f"{first} is {second}")
