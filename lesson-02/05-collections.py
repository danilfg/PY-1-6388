# while (standard loop), for ... in (python-style)
# zip, map, min, max

rooms = [100, 101, 102]
people = ['2 people', '10 people', 'empty']

print(list(zip(rooms, people)))

print(list(map(hex, rooms)))