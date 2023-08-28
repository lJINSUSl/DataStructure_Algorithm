import sys

N = int(sys.stdin.readline())
req = list(map(int,sys.stdin.readline().split()))
req.sort()

M = int(sys.stdin.readline())

lo = 0
hi = max(req)
mid = (lo + hi) //2
ans = 0

#파라매트릭 서치
def is_possible(mid):

    return sum(min(r,mid) for r in req) <= M


while lo <= hi:
    if is_possible(mid):
        lo = mid +1
        ans = mid
    else:
        hi = mid -1
    mid = (lo+hi)//2

print(ans)
