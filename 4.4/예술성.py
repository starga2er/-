from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

n = int(input())

nlist = [list(map(int,input().split())) for i in range(n)]
groups = []
groups_value = []
groups_dict = dict()

# 그룹화
visited = [[False]*n for i in range(n)]

def grouping():
    global visited
    groups = []
    groups_value = []

    for i in range(n):
        for j in range(n):
            if not visited[i][j] :
                new_group = make_group(j,i)
                for x, y in new_group:
                    groups_dict[(x,y)] = len(groups)
                groups.append(new_group)
                groups_value.append(nlist[i][j])
    
    return groups , groups_value

def make_group(x,y):
    global visited
    
    q =deque()
    q.append((x,y))
    visited[y][x] = True
    value = nlist[y][x]
    anslist = [(x,y)]

    while len(q) != 0:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <n and 0<= ny <n and not visited[ny][nx] and nlist[ny][nx] == value:
                anslist.append((nx,ny))
                visited[ny][nx] = True
                q.append((nx,ny))
    
    return anslist

def hamony(i,j):
    ans = 0

    for x, y in groups[i]:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <n and 0<= ny <n and groups_dict[(nx,ny)] == j:
                ans += 1

    return ans

def re_groups():
    new_list = [ [0]*n for i in range(n)]
    for i in range(n):
        new_list[n//2][i] = nlist[i][n//2]
        new_list[n-1-i][n//2] = nlist[n//2][i]
    
    for i in range(2):
        for j in range(2):
            for k in range(n//2):
                for l in range(n//2):
                    new_list[(n//2 + 1)*i + l ][(n//2 + 1)*j + n//2 -1 -k  ] = nlist[(n//2 + 1)*i + k][(n//2 + 1)*j + l ]
    return new_list

answer = 0
for t in range(4):
    # for l in range(n):
    #    print(nlist[l])
    # print('-')
    groups = []
    groups_value = []
    groups_dict = dict()
    visited = [[False]*n for i in range(n)]

    groups , groups_value = grouping()
    for i in range(len(groups)):
        for j in range(i+1,len(groups)):
            point = (len(groups[i]) + len(groups[j])) * groups_value[i] * groups_value[j] * hamony(i,j)
            answer += point
    # print(answer)
    if t == 3 :
        break
    nlist = re_groups()

print(answer)