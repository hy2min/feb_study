n=int(input())
name=['x','o']
path=[0]*n

def abc(level):
    if level==n:
        for i in range(n):
            print(path[i],end="")
        print()
        return

    for i in range(2):
        path[level] = name[i]
        abc(level+1)
        path[level] = 0

abc(0)