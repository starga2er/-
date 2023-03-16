N = int(input())

for i in range(N):
    n = int(input())
    clothes = dict()
    for j in range(n):
        _, wear = input().split()
        if wear in clothes.keys():
            clothes[wear] +=1
        else :
            clothes[wear] = 2
    num = 1
    for j in clothes.values():
        num *= j
    print(num-1)