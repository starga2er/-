N = int(input())
nlist = list(map(int,input().split()))
M = int(input())
mlist = list(map(int,input().split()))

nlist.sort()

def find(anwser):
    global nlist

    start = 0
    end = N-1

    while (start<= end):
        mid= (start+end)//2
        if nlist[mid]==anwser:
            return 1
        elif nlist[mid]<anwser:
            start = mid +1
        else :
            end = mid - 1
    return 0
    
for i in mlist:
    print(find(i))