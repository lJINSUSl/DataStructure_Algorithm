import sys
import math

N, K = map(int,sys.stdin.readline().split())

coins = [int(input()) for coin in range(N)]



num_coin = 0

while coins:
    if K < coins[-1]:
        coins.pop(-1)
    else:
        quotient = K / coins[-1]
        K = K % coins[-1]
        num_coin += math.floor(quotient)
        coins.pop(-1)
print(num_coin)

#정답코드

N, K = map(int,sys.stdin.readline().split())

coins = [int(input()) for coin in range(N)]
coins.reverse()
ans = 0
for coin in coins:
    ans += K // coin #몫 구하는 코드
    K %=coin
print(ans)






