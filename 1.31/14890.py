N, L = map(int, input().split())

llist = []
for i in range(N):
    llist.append(list(map(int, input().split())))

num = 0 

for i in range(N):
    rail = llist[i]
    level = rail[0]
    stack = 1

    n = 1
    while n != N and n != 0:
        if level == rail[n]:
            stack +=1
        elif rail[n] - level == 1:
            if stack < L:
                break
            else :
                stack = 1
                level = rail[n]
        elif level - rail[n] == 1:
            if n+L <= N:
                for k in range(n,n+L):
                    if rail[k] != rail[n]:
                        n =-1
                        break
                if n == -1 :
                    break
                n = n+L-1
                stack = 0
                level = rail[n]
            else :
                break
        else :
            break
        n +=1

    if n == N:
        num+=1

for i in range(N):
    rail = [llist[j][i] for j in range(N)]
    level = rail[0]
    stack = 1

    n = 1
    while n != N and n != 0:

        if level == rail[n]:
            stack +=1
        elif rail[n] - level == 1:
            if stack < L:
                break
            else :
                stack = 1
                level = rail[n]
        elif level - rail[n] == 1:
            if n+L <= N:
                for k in range(n,n+L):
                    if rail[k] != rail[n]:
                        n =-1
                        break
                if n == -1 :
                    break
                n = n+L-1
                stack = 0
                level = rail[n]
            else :
                break
        else :
            break
        n +=1

    if n == N:
        num+=1

print(num)