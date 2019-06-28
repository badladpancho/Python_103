number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
# lets say you want to print out every element it can be seen as a colomb and a row
# this will need two for loops
for row in number_grid:
    for col in row:
        print(row)