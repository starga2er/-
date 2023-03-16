K, N = map(int, input().split())

nlist = [int(input()) for _ in range(K)]

start = 1
end = max(nlist)
answer = 0

while (start<= end):
    mid= (start+end)//2
    ans = 0
    for i in nlist:
        ans += i//mid
    if ans < N:
        end = mid-1        
    else:
        start = mid + 1
        if mid > answer:
            answer = mid
print(answer)