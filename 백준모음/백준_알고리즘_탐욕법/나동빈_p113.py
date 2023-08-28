N = int(input())

import itertools

h = 60
m = 60
cnt = 0
for i in range(N+1):
    for j in range(h):
        for k in range(m):
            if '3' in str(i) + str(j) + str(k):

                cnt += 1

print(cnt)

