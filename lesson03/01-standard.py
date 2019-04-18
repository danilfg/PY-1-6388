# map, sum, min, max, filter
print(map(bin, [10, 20, 30]))

for x in map(bin, [10, 20, 30]):
    print(x)

numbers = [1, 2.4, 3.9, 4, 5.1, 6, 7]

print(list(filter(lambda x: x % 1 != 0, numbers)))

result = []
for x in numbers:
    if x % 1 != 0:
        result.append(x)
