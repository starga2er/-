m, t = map(int, input().split())
r, c = map(int, input().split())
r -= 1
c -= 1

dy = [-1,0,1,0]
dx = [0,-1,0,1]
mdx = [0,-1,-1,-1,0,1,1,1]
mdy = [-1,-1,0,1,1,1,0,-1]


nmap = []
for i in range(4):
    nlist = []
    for j in range(4):
        nlist.append([])
    nmap.append(nlist)

deadmon = [[0]*4 for i in range(4)]

for i in range(m):
    y, x, d = map(int, input().split())
    nmap[y-1][x-1].append(d-1)


def dfs(x, y):
    global dx ,dy,nmap, deadmon, r, c
    point = -1
    new = []
    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if 0<= x1 <4 and 0<= y1 <4 :
            for j in range(4):
                x2 = x1 + dx[j]
                y2 = y1 + dy[j]
                if 0<= x2 <4 and 0<= y2 <4 :
                    for k in range(4):
                        x3 = x2 + dx[k]
                        y3 = y2 + dy[k]
                        if 0<= x3 <4 and 0<= y3 <4 :
                            temp = len(nmap[y1][x1])
                            temp += len(nmap[y2][x2])
                            if (x1,y1) != (x3,y3):
                                temp += len(nmap[y3][x3])
                            if temp > point:
                                point = temp
                                new = [(x1,y1),(x2,y2),(x3,y3)]
    
    for x, y in new:
        # print(x,y)
        if len(nmap[y][x]) != 0 :
            deadmon[y][x] = 3
        nmap[y][x] = []
        r, c = y, x

            





for i in range(t):
    #몬스터 복제
    eggs = []
    for j in range(4):
        for k in range(4):
            for monster in nmap[j][k] :
                eggs.append((k,j,monster))

    #몬스터 이동
    new_map = []
    for i in range(4):
        nlist = []
        for j in range(4):
            nlist.append([])
        new_map.append(nlist)
    for j in range(4):
        for k in range(4):
            for mon_dir in nmap[j][k] :
                ny = j + mdy[mon_dir]
                nx = k + mdx[mon_dir]
                for tr in range(8):
                    if 0 <= ny < 4 and 0 <= nx < 4 and deadmon[ny][nx] == 0 and (nx,ny) != (c,r) :
                        break
                    else : 
                        mon_dir = (mon_dir+1)%8
                        ny = j + mdy[mon_dir]
                        nx = k + mdx[mon_dir]
                    
                    if tr == 7 :
                        ny = j
                        nx = k
                        break
                new_map[ny][nx].append( mon_dir)
    nmap = new_map

    #팩맨
    dfs(c,r)

    #몬스터 시체 소거
    for j in range(4):
        for k in range(4):
            if deadmon[j][k] != 0:
                deadmon[j][k] -= 1

    #부활
    for x, y , dir in eggs:
        nmap[y][x].append(dir)
    # for j in range(4):
    #    print(nmap[j])
    # print(c,r)
ans = 0
for j in range(4):
    for k in range(4):
        ans+=len(nmap[j][k])

# for j in range(4):
#    print(nmap[j])
print(ans)