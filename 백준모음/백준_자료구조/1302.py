import sys


N = int(sys.stdin.readline())
m = {}
for _ in range(N):
    book = sys.stdin.readline().strip()
    if book in m:
        m[book]= m[book]+1
    else:
        m[book] = 0
max_key = [key for key,value in m.items() if max(m.values()) == value]
max_key.sort()
print(max_key[0])