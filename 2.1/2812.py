N, K = map(int,input().split())
num = list(input())

answer = []
lens = N-K
for n in num:
    while answer and K > 0 and answer[-1] < n:
        del answer[-1]
        K -=1
    answer.append(n)


print(''.join(answer[:lens]))