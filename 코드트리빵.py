import copy
from collections import deque

dy = [-1,0,0,1]
dx = [0,-1,1,0]
n, m = map(int,input().split())

nlist = [[0]*n for i in range(n)]
base_camp = []
dest = []
people = []

for i in range(n):
    new_temp = list(map(int,input().split()))
    for j in range(n):
        if new_temp[j] == 1 :
            base_camp.append((j,i))

for i in range(m):
    y, x = map(int,input().split())
    dest.append((x-1,y-1))

def check_base(num):
    global dest, base_camp, nlist,people
    candidates = []
    x, y = dest[num]
    for nx,ny in base_camp:
        candidates.append((abs(x-nx)+abs(y-ny), ny,nx))
    _,ny,nx= min(candidates)
    base_camp.remove((nx,ny))
    nlist[ny][nx] = 1
    people.append([num, nx,ny])

def dfs(x,y, num):
    global dest, nlist,n,dx,dy
    if not(0 <= x < n and 0 <= y < n and nlist[y][x] == 0):
        return -1

    visited = [[0]*n for i in range(n)]
    visited[y][x] = 1
    queue = deque()
    queue.append((x,y,0))
    while len(queue) != 0:
        x, y, way = queue.popleft()
        if (x,y) == dest[num]:
            return way

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and nlist[ny][nx] == 0 and visited[ny][nx]== 0:
                visited[ny][nx]=1
                queue.append((nx,ny,way+1))
    return -1

    

def move():
    global people
    for i in range(len(people)):
        num, x, y = people[i]
        togo = 0
        minway = 15*15
        for j in range(4):
            ans = dfs(x + dx[j],y+dy[j],num)
            if ans == -1 :
                continue
            elif minway > ans:
                minway = ans
                togo = j
        people[i][1] = x + dx[togo]
        people[i][2] = y + dy[togo]
        

def stop() :
    global dest, nlist
    for i in reversed(range(len(people))):
        num, x, y = people[i]
        if dest[num] == (x,y):
            nlist[y][x] =1 
            del people[i]

time = 0
while time < m or len(people) != 0:
    move()
    stop()
    if time < m :
        check_base(time)
    time += 1
    print(people)
    # print(nlist)
print(time)