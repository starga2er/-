from itertools import combinations

N, m= map(int, input().split())
mmap = [list(map(int, input().split())) for _ in range(N)]
chicken_num = []
house_num = 0
for i in range(N):
    for j in range(N):
        if mmap[i][j] == 2:
            chicken_num.append((i, j))
        if mmap[i][j] == 1:
            house_num += 1
ans = 987654321

distance_map = []

for k in range(len(chicken_num)):
    distance = []
    for i in range(N):
        for j in range(N):
            if mmap[i][j] == 1:
                distance.append(abs(i-chicken_num[k][0]) + abs(j-chicken_num[k][1]))
    distance_map.append(distance)

def min_distance(chosen_chicken):
    dis = []
    ret = 0
    for i in chosen_chicken:
        dis.append(distance_map[i])
    for i in range(house_num):
        ret += min([dis[j][i] for j in range(m)])
    return ret
    
for i in combinations(range(len(chicken_num)), m) :
    ans= min (ans,min_distance(i))
print(ans)