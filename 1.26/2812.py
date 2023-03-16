N, K = map(int,input().split())
n = input()
ans = ''

def Node():
    def __init__(self, data):
        self.data = data
        self.next = None

s = Node(0)
start = s
for i in n:
    k = Node(int(i))
    s.next = k
    s = k


for j in range(K+1):
    s= start
    for i in range(N):
        if s.next.data <= s.next.next.data
print(ans)