arr = [i for i in map(int,input().split())]

for i in arr:
    if i < 20:
        print("더 큰수를 입력하세요")
    if i > 20:
        print("더 작은수를 입력하세요")
    if i == 20:
        print("정답입니다")