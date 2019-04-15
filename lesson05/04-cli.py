import sys

# variables
intro_message = "Starting app..."
exit_message = "Closed"


# functions definition
def hello():
    print("First message of this app")


def super_hello(name):
    print(f"First message for {name}")


# functions dict
dict_functions = {
    "h": hello,
    "H": super_hello
}

# main loop
arguments = sys.argv[1:]

print(intro_message)

if dict_functions.get(arguments[0]):
    dict_functions[arguments[0]]()
else:
    print('Invalid command')

# if len(arguments) > 0:
#     name = arguments[0]
#     super_hello(name)
# else:
#     hello()

print(exit_message)
