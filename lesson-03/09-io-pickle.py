# DEPRECATED
# create, write, load
user = {
    "name": "John",
    "age": 30,
    "favorite_colors": ['red', 'green', 'blue']
}

file_pickle = open('data.bin', 'wb')

import pickle

pickle.dump(user, file_pickle)