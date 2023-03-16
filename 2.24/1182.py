N, S = map(int,input().split())

nlist = list(map(int,input().split()))


n = 0

def dfs(num, i):
    global n
    if i == N :
        return
    else :
        dfs(num,i+1)
        if num+nlist[i] == S :
            n += 1
        dfs(num+nlist[i], i+1)

dfs(0,0)
print(n)