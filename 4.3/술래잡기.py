dx = [1,0,-1,0]
dy = [0,1,0,-1]

n, m, h, k = map(int, input().split())
sx, sy = n//2 , n//2
dir = 3
tick = 2
w = 1


trees = [[False]*n for i in range(n)]
nlist = [[[] for i in range(n)] for j in range(n)]

for i in range(m):
    y, x, d = map(int, input().split())
    y -= 1
    x -= 1
    d -= 1
    nlist[y][x].append(d)

for i in range(h):
    y, x = map(int, input().split())
    trees[y-1][x-1] = True

runable = []
for i in range(-3,4):
    for j in range(-3,4):
        if abs(i) + abs(j) <= 3:
            runable.append((i,j))

def run():
    global nlist
    new_list = [[[] for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if abs(i-sy) +abs(j-sx) <= 3:
                for k in nlist[i][j]:
                    nx, ny = j + dx[k], i + dy[k]
                    if not (0<= nx < n and 0<= ny <n):
                        k = (k+2)%4
                        nx, ny = j + dx[k], i + dy[k]

                    if (nx,ny) == (sx,sy):
                        new_list[i][j].append(k)
                    else :
                        new_list[ny][nx].append(k)

            else :
                for k in nlist[i][j]:
                    new_list[i][j].append(k)
    nlist = new_list

def catch_runner():
    global sx, sy, dir, w

    nx, ny = sx + dx[dir], sy + dy[dir]
    if (nx,ny) == (0,0) or (nx,ny) == (n//2,n//2):
        dir = (dir+2)%4
        w *= -1 #돌아올때 태케 조심
    elif nx+ny == n-1:
        dir = (dir+w)%4
    elif nx > n//2 and nx == ny :
        dir = (dir+w)%4
    elif nx <= n//2 and nx == ny + 1 :
        dir = (dir+w)%4

    sx, sy = nx, ny

    catched = 0
    for i in range(3):
        see_x, see_y = sx+dx[dir]*i, sy+dy[dir]*i
        if 0<= see_x< n and 0<= see_y <n and not trees[see_y][see_x]:
            catched += len(nlist[see_y][see_x])
            nlist[see_y][see_x] = []
    return catched


answer = 0    
for i in range(k):
    run()
    answer += (i+1)*catch_runner()
print(answer)

# for i in range(n):
#     print(nlist[i])

#벗어난경우
#아닌경우

#술래는 달팽이모양