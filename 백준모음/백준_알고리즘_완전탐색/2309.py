import sys
from itertools import combinations

s = []
for _ in range(9):
    num = int(sys.stdin.readline())
    s.append(num)
s.sort()

for number in combinations(s,7):
    if sum(number) == 100:
        for n in number:
            print(n)
        break

