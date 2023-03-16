n, m, k = map(int, input().split())
nlist =[]
players=[]
point = [0] * m
dy = [-1,0,1,0]
dx = [0,1,0,-1]

def intlist(n):
    return [int(n)]

for _ in range(n):
    nlist.append(list(map(intlist, input().split())))

class player:
    n = n
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    map = nlist
    moving_map = []

    def __init__(self, x,y,d,s,n):
        self.x = y-1
        self.y = x-1
        self.dir = d
        self.stat = s
        self.num = n
        self.gun = 0
        player.moving_map.append((self.x,self.y))
    
    def move(self):
        ny, nx = self.y + dy[self.dir], self.x + dx[self.dir]
        if 0<= ny < player.n and 0<= nx < player.n :
            self.y = ny
            self.x = nx
        else :
            self.dir = (self.dir+2)%4
            self.y = self.y + dy[self.dir]
            self.x = self.x + dx[self.dir]
        player.moving_map[self.num] = (self.x,self.y)
    
    def run(self) :

        ny, nx = self.y + dy[self.dir], self.x + dx[self.dir]
        while not( 0<= ny < player.n and 0<= nx < player.n and not (nx,ny) in player.moving_map):
            self.dir = (self.dir+1)%4
            ny, nx = self.y + dy[self.dir], self.x + dx[self.dir]
        self.y = ny
        self.x = nx
        player.moving_map[self.num] = (self.x,self.y)

    def drop_gun(self):
        player.map[self.y][self.x].append(self.gun)
        self.gun = 0
    
    def get_gun(self):
        self.drop_gun()
        self.gun = max(player.map[self.y][self.x])
        player.map[self.y][self.x].remove(self.gun)

def fight(p1 : player, p2 : player):
    global point, players
    _, __, winner = max([(p1.stat + p1.gun, p1.stat,p1.num) , (p2.stat + p2.gun, p2.stat,p2.num)])
    _, __, losser = min([(p1.stat + p1.gun, p1.stat,p1.num) , (p2.stat + p2.gun, p2.stat,p2.num)])
    point[winner] += abs(p1.stat + p1.gun - p2.stat - p2.gun)
    p1.drop_gun()
    p2.drop_gun()
    players[winner].get_gun()
    players[losser].run()


for i in range(m):
    players.append(player(*(map(int, input().split())),i))

for _ in range(k):
    for i in range(m):
        players[i].move()
        rest_list = list(filter(lambda x: player.moving_map[x] == (players[i].x,players[i].y), range(m)))
        if len(rest_list) == 1:
            players[i].get_gun()
        elif len(rest_list) == 2:
            fight(players[rest_list[0]], players[rest_list[1]])
        else:
            print('error')
print(*point)
