from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

n = int(input())
coins = dict()
coins_list = []
dp = [[0]*11 for _ in range(11)]

nlist =[]
for i in range(n):
    text = input()
    n_list = []
    for j in range(n):
        if text[j] == '.':
            n_list.append(0)
        elif text[j] == '#':
            n_list.append(1)
        elif text[j] == 'S':
            n_list.append(0)
            coins[0] = (j,i)
        elif text[j] == 'E':
            n_list.append(0)
            coins[10] = (j,i)
        else:
            n_list.append(0)
            coins[int(text[j])] = (j,i)
    nlist.append(n_list)

coins_list = list(coins.keys())
coins_list.sort()


def dfs(start, end):
    visited = [[False] *n for i in range(n)]
    q = deque()
    sx, sy = coins[start]
    ex, ey = coins[end]
    q.append((sx,sy, 0))
    visited[sy][sx] = True

    while len(q) != 0:
        x,y, way = q.popleft()
        if (x,y) == (ex,ey):
            return way

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < n and nlist[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((nx,ny,way+1))

    return -1

for i in range(len(coins_list)):
    for j in range(i+1, len(coins_list)):
        dp[coins_list[i]][coins_list[j]] = dfs(coins_list[i],coins_list[j])


ans = 400 * 400 * 400
for i in range(1, len(coins_list)-1):
    for j in range(i+1, len(coins_list)-1):
        for k in range(j+1, len(coins_list)-1):
            way1 = dp[0][coins_list[i]] 
            way2 = dp[coins_list[i]][coins_list[j]]
            way3 = dp[coins_list[j]][coins_list[k]]
            way4 = dp[coins_list[k]][10]
            if -1 in [way1, way2, way3, way4]:
                continue
            elif ans > way1+ way2 + way3 + way4:
                ans = way1+ way2 + way3 + way4

if ans == 400 * 400 * 400 :
    print(-1)
else :
    print(ans)
