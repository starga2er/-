from functools import lru_cache
from collections import deque

@lru_cache(maxsize=5**2)
def get_cost_(a, b):
    if a == b:
        return 1
    if a == 0 or b == 0:
        return 2
    if (a + b) % 2 == 0:
        return 4
    return 3

@lru_cache(maxsize=5**4)
def get_cost(a, b, c, d):
    '''
    a, b -> c, d
    '''
    if a == c and b == d:
        return 1
    if a == c:
        return get_cost_(b, d)
    if b == d:
        return get_cost_(a, c)

cmds = list(map(int, input().split()))

if cmds[0] == 0:
    print(0)
else:
    dp = [{}, None]

    dp[0][(0, 0)] = 0

    for cmd in cmds[0:-1]:
        dp[1] = {}
        
        for a, b in dp[0]:
            if a != cmd:
                if (a, cmd) not in dp[1]:
                    dp[1][(a, cmd)] = 10 ** 9
                dp[1][(a, cmd)] = min(dp[1][(a, cmd)], dp[0][(a, b)] + get_cost(a, b, a, cmd))
            if b != cmd:
                if (cmd, b) not in dp[1]:
                    dp[1][(cmd, b)] = 10 ** 9
                dp[1][(cmd, b)] = min(dp[1][(cmd, b)], dp[0][(a, b)] + get_cost(a, b, cmd, b))
        
        dp[0], dp[1] = dp[1], dp[0]

    print(min(dp[0][k] for k in dp[0]))