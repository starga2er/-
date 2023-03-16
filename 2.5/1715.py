import sys

N = int(input())

class heap:
    def __init__(self):
        self.heapl = [0]

    def push(self, n):
        self.heapl.append(n)
        x = len(self.heapl)-1
        while (n > self.heapl[x//2] and x != 1):
            self.heapl[x] = self.heapl[x//2]
            self.heapl[x//2] = n
            x = x//2
    
    def pop(self):
        if len(self.heapl) == 1:
            return 0

        answer = self.heapl[1]
        self.heapl[1] = self.heapl[-1]
        del self.heapl[-1]
        if len(self.heapl) == 1:
            return answer
        n = self.heapl[1]
        x = 1
        while (x < len(self.heapl)):
            large, small = x*2 , x*2+1
            if (x*2 >= len(self.heapl)):
                break

            if (x*2+1 >= len(self.heapl)):
                large = x*2
            elif (self.heapl[x*2] < self.heapl[x*2+1]):
                large, small = x*2+1, x*2  
            
            if (self.heapl[x] < self.heapl[large]):
                self.heapl[x] = self.heapl[large]
                self.heapl[large] = n
                x = large
            else:
                break
        return answer


h = heap()
for i in range(N):
    k = int(sys.stdin.readline())
    h.push(-k)

ans = 0
while(len(h.heapl) != 2):
    f1 = -h.pop()
    f2 = -h.pop()
    cards = f1+f2
    ans += cards
    h.push(-cards)

    

print(ans)
