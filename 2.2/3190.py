from collections import deque

dy = [0,1,0,-1]
dx = [1,0,-1,0]
x, y = 0, 0 

N = int(input())
board = [ [0]*N for i in range(N)]

K = int(input())
for i in range(K):
    a, b = map(int,input().split())
    board[a-1][b-1] = 1

L = int(input())
turn = {}
for i in range(L):
    a, b= input().split()
    turn[int(a)] = b

snake = deque()
snake.append((0,0))
tick = 0
direction = 0
board[y][x] = 2

def turning(n):
    global direction
    if n == 'D':
        direction = (direction+1)%4
    else:
        direction = (direction-1)%4

while(True):
    tick +=1
    y, x = y + dy[direction], x + dx[direction]
    if 0 <= y < N and 0 <= x < N and board[y][x] != 2:
        if not board[y][x] == 1:
            dely, delx = snake.popleft()
            board[dely][delx] = 0
        board[y][x] = 2
        snake.append((y,x))
        if tick in turn.keys():
            turning(turn[tick])
    else :
        break
print(tick)