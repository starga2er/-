N, M = map(int, input().split())
nlist = list(map(int, input().split()))
querys = []
for i in range(M):
    x,y = map(int,input().split())
    querys.append((x-1,y-1))

top = N
bottom = 1
mid = (N+1)//2

while True:
    new_list = []
    # print(bottom, mid, top)
    for i in range(N):
        if mid < nlist[i]:
            new_list.append(0)
        elif mid > nlist[i]: 
            new_list.append(-1)
        else :
            new_list.append(mid)
    for i in querys:
        # print(new_list)
        if i[0] < i[1]:
            n1 = 0
            ifmid = False
            for j in range(i[0], i[1]+1):
                if new_list[j] == -1:
                    n1 += 1
                elif new_list[j] == mid :
                    ifmid = True
            for j in range(i[0], i[0]+n1):
                new_list[j] = -1
            if ifmid:
                new_list[i[0]+n1] = mid
                n1 +=1
            for j in range(i[0]+n1, i[1]+1):
                new_list[j] = 0
        else :
            n0 = 0
            ifmid = False
            for j in range(i[1], i[0]+1):
                if new_list[j] == 0:
                    n0 += 1
                elif new_list[j] == mid :
                    ifmid = True
            for j in range(i[1], i[1]+n0):
                new_list[j] = 0
            if ifmid:
                new_list[i[1]+n0] = mid
                n0 +=1
            for j in range(i[1]+n0, i[0]+1):
                new_list[j] = -1
    if new_list[(N+1)//2 -1] == mid:
        break
    elif new_list[(N+1)//2 -1] == 0:
        bottom = mid
        mid = (top+bottom + 1) // 2
    else:
        top = mid
        mid = (top + bottom) // 2

print(mid)