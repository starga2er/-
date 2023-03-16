from collections import deque

N, M, K = map(int,input().split())

nmap = [[5]*N for _ in range(N)]
Alist = [ list(map(int,input().split())) for i in range(N)]
trees = [[deque() for _ in range(N) ]for _ in range(N)]
for i in range(M):
    y, x, z = map(int,input().split())
    trees[y-1][x-1].append(z)

for year in range(K):
    #봄, 여름
    newtrees = []
    for i in range(N):
        for j in range(N):
            for k in range(len(trees[i][j])):
                if nmap[i][j] >= trees[i][j][k]:
                    nmap[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
                    if trees[i][j][k]%5==0:
                        newtrees.append((i,j))
                else:
                    for l in range(len(trees[i][j])-k):
                        nmap[i][j] += trees[i][j].pop()//2 # 각각이라는 이유로 틀렸다
                    break
    
    #가을
    for y,x in newtrees:
        for i in [1,0,-1]:
            for j in [1,0,-1]:
                nx = x+j
                ny = y+i
                if (i,j) != (0,0) and 0<= nx < N and 0<= ny <N:
                    trees[ny][nx].appendleft(1)
    #겨울
    for i in range(N):
        for j in range(N):
            nmap[i][j] += Alist[i][j]
  
num = 0
for i in range(N):
    for j in range(N):
        num += len(trees[i][j])
print(num)