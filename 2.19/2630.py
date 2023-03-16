N = int(input())

nlist = [list(map(int, input().split())) for _ in range(N)]

papers = [0,0]

def dp(nmap) :
    length = len(nmap)
    if length == 1 :
        if nmap[0][0] != 2:
            papers[nmap[0][0]] += 1
        return
    newmap = []
    for i in range(length//2):
        newnmap = []
        for j in range(length//2):
            if nmap[2*i][2*j] == nmap[2*i+1][2*j] == nmap[2*i][2*j+1] == nmap[2*i+1][2*j+1] == 0 :
                newnmap.append(0)
            elif nmap[2*i][2*j] == nmap[2*i+1][2*j] == nmap[2*i][2*j+1] == nmap[2*i+1][2*j+1] == 1 :
                newnmap.append(1)
            else :
                for n in range(2):
                    for m in range(2):
                        if nmap[2*i+n][2*j+m] !=2:
                            papers[nmap[2*i+n][2*j+m]] +=1
                newnmap.append(2)
        newmap.append(newnmap)
    return dp(newmap)

dp(nlist)
print(papers[0])
print(papers[1])
