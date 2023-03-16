n = int(input())
p1, p2 = map(int,input().split())
p1, p2 = p1-1,p2-1
m = int(input())

jokbo = dict()
for i in range(m):
    x, y = map(int,input().split())
    x, y = x-1, y-1
    if x in jokbo.keys():
        jokbo[x].append(y)
    else :
        jokbo[x] = [y]


jokbo2 = [[0]*n for i in range(n) ]

for i in jokbo.keys():
    josang = i
    jason = jokbo[i]
    for j in jason:
        jokbo2[josang][j] = 1
        jokbo2[j][josang] = 1
        for k in jason :
            if j != k:
                jokbo2[j][k] = 2
        
ans = -1
check = [-1]*n


def dfs(q,chon):
    for i in range(n):
        if (jokbo2[q][i] != 0 and check[i] == -1):
            check[i] = jokbo2[q][i] + chon
    for i in range(n):
        if (jokbo2[q][i] != 0 and check[i] == jokbo2[q][i] + chon):
            dfs(i,check[i])
    
dfs(p1,0)

print(check[p2])