def hanoi(n, start,to,end):
    if n == 1:
        print(start, end)
    else:
        hanoi(n-1, start, end, to)
        print(start, end)
        hanoi(n-1, to, start, end)
num = int(input())
print(2**num -1)
if num <= 20:
    hanoi(num,1,2,3)