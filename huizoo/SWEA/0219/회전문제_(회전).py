t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{tc} {arr[M%N]}')