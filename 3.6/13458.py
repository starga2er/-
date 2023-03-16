N = int(input())
nlist = list(map(int,input().split()))
B, C = map(int,input().split())

num = 0 

for i in nlist:
    if i <= B :
        num += 1
    else :
        num += (i-B-1)//C + 2
print(num)