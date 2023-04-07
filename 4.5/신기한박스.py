from collections import deque
from copy import deepcopy

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

move_map = [[]]

def init(n):
    return int(n)-1

n = int(input())

for i in range(8):
    move_map.append(list(map(init, input().split())))

cmd = [list(map(int,input().split())) for i in range(n)]

def moving(nmap : deque):
    new_map = deque([[0]*4 for _ in range(105)])

    for i in range(4):
        for j in reversed(range(105)):
            if nmap[j][i] == 0 :
                break
            else:
                num = nmap[j][i]
                for k in range(8):
                    nx = i + dx[move_map[num][k]]
                    ny = j + dy[move_map[num][k]]

                    if 0 <= nx < 4 and 0<= ny < 105 :
                        if new_map[ny][nx] == 0 or new_map[ny][nx] > num:
                            new_map[ny][nx] = num
                        break

    return all_drop(new_map)

def all_drop(nmap : deque):
    for i in range(4):
        bottom = 105
        for j in reversed(range(105)):
            if nmap[j][i] != 0 :
                bottom -= 1
                if bottom != j:
                    nmap[bottom][i] = nmap[j][i]
                    nmap[j][i] = 0 
    return nmap


def check_point(nmap : deque):
    point = 0
    for i in reversed(range(105)):
        if not 0 in nmap[i]:
            point += 1
        else :
            break
    for i in range(point):
        nmap.pop()
        nmap.appendleft([0,0,0,0])
    return point, nmap

def drop_bucket(k,c ,nmap : deque):
    for i in reversed(range(105)):
        if nmap[i][c] == 0:
            nmap[i][c] = k
            break
        else :
            pass
    return nmap

ans = 0

def dp(i,nmap, points):
    global ans
    if i == n :
        ans = max(ans,points)
        return
    k, c = cmd[i]
    if c != 0 :
        nmap = drop_bucket(k, c-1, nmap)
        point, nmap = check_point(nmap)
        points += point


        nmap = moving(nmap)

        point, nmap = check_point(nmap)
        points += point
        

        return dp(i+1,nmap, points)
    else :
        for j in range(4):
            cnmap = deepcopy(nmap)
            
            cnmap = drop_bucket(k,j, cnmap)
            point, cnmap = check_point(cnmap)
            cpoints = point + points
            
            cnmap = moving(cnmap)
            point, cnmap = check_point(cnmap)
            cpoints = point + cpoints
            
            dp(i+1,cnmap, cpoints)

dp(0, deque([[0]*4 for _ in range(105)]) , 0)
print(ans)