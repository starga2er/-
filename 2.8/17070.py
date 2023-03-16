N = int (input())
nlist = [[1]*(N+2) for _ in range(N+2)]
for i in range(1, N+1):
    l = list(map(int,input().split()))
    for j in range(1,N+1):
        nlist[i][j] = l[j-1]
types = ['가로', '세로', '대각선']

ans = 0
def dfs(y,x, type):
    global ans
    if (y,x) == (N,N):
        ans += 1
    else :
        if type == '가로' or type == '대각선':
            if nlist[y][x+1] == 0:
                dfs(y,x+1,'가로')
        if type == '세로' or type == '대각선':
            if nlist[y+1][x] == 0:
                dfs(y+1,x,'세로')
        if nlist[y+1][x+1] == 0 and nlist[y][x+1] == 0 and nlist[y+1][x] == 0:
                dfs(y+1,x+1,'대각선')
dfs(1,2, '가로')
print(ans)