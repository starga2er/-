#   1
# 3 0 2
#   4
#   5

roll = [6,2,3,4,5,1]

rx = [1,0,-1,0] # 동 남 서 북
ry = [0,1,0,-1]

def dice_roll(roll, type):
    if type == 0:
        temp = roll[2]
        roll[2] = roll[5]
        roll[5] = roll[3]
        roll[3] = roll[0]
        roll[0] = temp
    elif type == 2:
        temp = roll[3]
        roll[3] = roll[5]
        roll[5] = roll[2]
        roll[2] = roll[0]
        roll[0] = temp
    elif type == 3:
        temp = roll[1]
        roll[1] = roll[5]
        roll[5] = roll[4]
        roll[4] = roll[0]
        roll[0] = temp
    elif type == 1:
        temp = roll[4]
        roll[4] = roll[5]
        roll[5] = roll[1]
        roll[1] = roll[0]
        roll[0] = temp
    return roll

N,M,K = map(int,input().split())

score_map = [[-1]*M for _ in range(N)]

mmap = [list(map(int,input().split())) for _ in range(N)]

temp_set = set()
def dfs(x,y,num):
    global temp_set
    if 0 <= x < M and 0 <= y < N and mmap[y][x] == num and not (x,y) in temp_set:
        temp_set.add((x,y))
        for i in range(4):
            dfs(x+rx[i], y+ry[i],num)

for i in range(N):
    for j in range(M):
        if score_map[i][j] == -1:
            dfs(j,i,mmap[i][j])
            for k in temp_set :
                score_map[k[1]][k[0]] = len(temp_set) * mmap[i][j]
            temp_set.clear()


x = 0
y = 0

move = 0
ans = 0

for i in range(K):
    dx = rx[move]
    dy = ry[move]

    if not (0 <= dx + x < M and 0 <= dy + y < N):
        move = (move+2)%4
        dx = rx[move]
        dy = ry[move]
    x = dx + x
    y = dy + y
    roll = dice_roll(roll, move)

    if mmap[y][x] < roll[0]:
        move = (move+1)%4
    elif mmap[y][x] > roll[0]:
        move = (move+3)%4
    ans += score_map[y][x]

print(ans)

"""
4 5 10
4 1 2 3 3
6 1 1 3 3
5 6 1 3 2
5 5 6 5 5
"""