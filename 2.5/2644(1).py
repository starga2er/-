n = int(input())
p1, p2 = map(int,input().split())
p1, p2 = p1-1,p2-1
m = int(input())

jokbo = [[0]*n for i in range(n)]
for i in range(m):
    x, y = map(int,input().split())
    x, y = x-1, y-1
    jokbo[x][y]=1
    jokbo[y][x]=1

check = [-1]*n


def dfs(q,chon):
    for i in range(n):
        if (jokbo[q][i] != 0 and check[i] == -1):
            check[i] = jokbo[q][i] + chon
    for i in range(n):
        if (jokbo[q][i] != 0 and check[i] == jokbo[q][i] + chon):
            dfs(i,check[i])
    
dfs(p1,0)

print(check[p2])