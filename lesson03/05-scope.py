# function scope, multi-level functions
a, b = 10, 20
d = 100


def summ(a, b):
    c = 10
    print(d)  # не надо так
    print(a + b)

print(c)  # error
summ(a, b)
