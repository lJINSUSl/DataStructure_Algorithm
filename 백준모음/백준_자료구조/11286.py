import sys
import heapq

T = int(sys.stdin.readline())

hq = []

for _ in range(T):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(hq,(abs(num),num))
    elif num == 0:
        if len(hq) == 0:
            print('0')
        elif len(hq) == 1:
            print(heapq.heappop(hq)[1])
        else:
            if hq[0][0] == hq[1][0]:
                if hq[0][1] < 0:
                    print(heapq.heappop(hq)[1])
                else:
                    dummy = heapq.heappop(hq)
                    print(heapq.heappop(hq)[1])
                    heapq.heappush(hq,dummy)
            else:
                print(heapq.heappop(hq)[1])



'''
#정답 코드

import heapq as hq
import sys

input = sys.stdin.readline
pq = []

for _ in range(int(input())):
    x = int(input())
    if x != 0:
        hq.heappush(pq,(abs(x),x))
    else:
        print(hq.heappop(pq)[1] if pq else 0)

'''

