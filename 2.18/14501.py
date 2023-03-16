import sys
limit_number = 2000000
sys.setrecursionlimit(limit_number)

N = int(input())
nlist = []

for _ in range(N):
    nlist.append(tuple(map(int, sys.stdin.readline().split())))

save = [0]*(N+1)
for i in reversed(range(N)):
    obj = nlist[i]
    if obj[0] + i <= N:
        save[i] = max(save[i+1],save[obj[0] + i]+obj[1])
    else:
        save[i] = save[i+1]


print(save[0])

