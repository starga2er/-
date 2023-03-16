from collections import deque

q = deque()

for i in range(0,int(input())):
    q.append(i)
while (True):
    a=q.popleft()
    if len(q) == 0:
        print(a+1)
        break
    elif len(q) == 1:
        print(q.popleft()+1)
        break
    else : 
        q.append(q.popleft())
