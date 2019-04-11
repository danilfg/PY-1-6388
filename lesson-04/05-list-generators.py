# generate numbers
nums = [x ** 2 for x in range(10)]

# convert string to numbers list
number = 123456
number_str = [int(x) for x in str(number)]

# filter list by rule
# filtered_list = filter(lambda x: x % 2 == 0, number_str)
filtered_list = [x for x in number_str if x % 2 == 0]

# dict generator (zip)
names = ['Artur', 'John']
roles = ['Admin', 'Manager']

# dict_example = {"key": "value"}
# result = dict(zip(names, roles))  # <zip object>

result = {key: value for key, value in zip(names, roles)}
