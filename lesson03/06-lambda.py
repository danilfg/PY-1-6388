# use lambda functions
# a = lambda x: int(x) * 2


def convert(x):
    return int(x) * 2


map(lambda x: int(x) * 2, [10, 20, 30])
map(convert, [10, 20, 30])
