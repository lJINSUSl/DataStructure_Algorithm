import sys

N, M, K = map(int, sys.stdin.readline().split())
ary = list(map(int, sys.stdin.readline().split()))

sorted_list = sorted(ary,reverse=True)

sum = 0
stk = 0
for _ in range(M):

    stk += 1
    if stk == K:
        sum += sorted_list[1]
        stk = 0
    else:
        sum += sorted_list[0]
print(sum)