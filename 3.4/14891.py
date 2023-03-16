gears = [input() for i in range(4)]
gear_nums = [0] * 4

N = int(input())
nlist = []
points = 0
def dfs(start, now, cycle):
    global points
    if start <= now :
        right = now + 1
        if right < 4 and gears[now][(gear_nums[now]+2)%8] != gears[right][(gear_nums[right]-2)%8] :
            dfs(start, right, -cycle)
    if start >= now :
        left = now - 1
        if 0 <= left and gears[now][(gear_nums[now]-2)%8] != gears[left][(gear_nums[left]+2)%8] :
            dfs(start, left, -cycle)

    gear_nums[now] = (gear_nums[now] - cycle)%8

for _ in range(N):
    gearnum, dir = map(int, input().split())
    dfs(gearnum-1, gearnum-1, dir)
for i in range(4):
    if gears[i][gear_nums[i]] == '1' :
        points += 2**i
print(points)