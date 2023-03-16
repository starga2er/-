N, M = map(int,input().split())

board1 = """WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW"""
board2 = """BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB"""

board = ""
for i in range(N):
    board += input()

ans = M*N

def compareb(a,b):
    ans = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            ans +=1
    return ans

for i in range(N-7):
    for j in range(M-7):
        compare_board = ""
        for k in range(8):
            compare_board += board[j+M*(i+k): j+M*(i+k)+8]

        dap = min(compareb(compare_board,board1),compareb(compare_board,board2))
        if ans > dap:
            ans =dap
print(ans)

# 문자열 \n같은거 생각하면서 풀기