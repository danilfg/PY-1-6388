# define
a = [1, 2, 3]
b = [1, 2, [1, 2], a]

# full copy (deepcopy)
from copy import deepcopy

c = deepcopy(b)

# matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# recursive print
row = 0
column = 0

while row < len(matrix):
    while column < len(matrix[row]):
        print(f"MATRIX[{row}][{column}] = {matrix[row][column]}")
        column += 1

    row += 1

# for .. in --> MATRIX[x][y] = VALUE
for row, row_value in enumerate(matrix):
    for column, column_value in enumerate(row_value):
        print(f"MATRIX[{row}][{column}] = {column_value}")

# real-world examples
plans = {'basic': 0, 'advanced': 1, 'corp': 2}

prices = [
    ['10gb', 100],
    ['25gb', 200],
    ['100gb', 400],
]

prices[plans['basic']]
