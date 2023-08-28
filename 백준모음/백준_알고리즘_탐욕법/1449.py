import sys

N, L = map(int,sys.stdin.readline().split())

data = list(map(int,sys.stdin.readline().split()))
data.sort()

ans = 0

while data:
    cover_range = data[0] + L - 0.5
    while data and (data[0] < cover_range):
        data.pop(0)
    ans += 1
print(ans)