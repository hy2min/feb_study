up = list(map(int, input().split()))
down = list(map(int, input().split()))
cnt = 0

for i in range(len(up)):
    if up[i] == down[i] == 1:
       cnt += 1

print(str(cnt)+"개")
