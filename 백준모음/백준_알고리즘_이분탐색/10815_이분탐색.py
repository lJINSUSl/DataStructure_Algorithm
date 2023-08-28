import sys
from bisect import bisect_left,bisect_right

N = int(sys.stdin.readline())
cards = sorted(list(map(int,sys.stdin.readline().split())))
M = int(sys.stdin.readline())
qry = list(map(int,sys.stdin.readline().split()))

ans = []

for q in qry:
    if bisect_left(cards,q) - bisect_right(cards,q) == 0:
        ans.append(0)
    else:
        ans.append(1)

print(*ans)
# print(','.join(map(str,ans)))