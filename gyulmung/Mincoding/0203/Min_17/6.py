arr1 = [[0, 0, 0, 1], [1, 1, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]]
arr2 = [[1, 1, 1, 1], [1, 0, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]]

for i in range(4):
    for j in range(4):
        if arr1[i][j] == 0 and arr2[i][j] == 0:
            print(f'({i},{j})')