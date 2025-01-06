#2D LISTS / MATRIX

matrix = [
    [1, 2, 3],
    [20, 30, 40],
    [400, 500, 600]
]

print(matrix[2][1]) # fetching 500 by getting the index of the 3rd(2) list and the 2nd(1) item

for row in matrix: #accesses each row in 2D List
    for item in row:
        print(item) #prints all the items in each row