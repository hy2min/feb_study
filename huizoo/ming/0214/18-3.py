arr = [
    [1,3,3,5,1],
    [3,6,2,4,2],
    [1,9,2,6,5],
]
n = int(input())
dat = [0]*10
for i in range(3):
    for j in range(5):
        dat[arr[i][j]] += 1
for i in range(10):
    if dat[i] == n:
        print(i, end = ' ')