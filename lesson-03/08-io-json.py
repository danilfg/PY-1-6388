# create, write, load
user = {
    "name": "John",
    "age": 30,
    "favorite_colors": ['red', 'green', 'blue']
}

import json

file_json = open('data.json', 'w')
json.dump(user, file_json)
# user = json.load()