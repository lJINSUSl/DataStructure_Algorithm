import sys
n = int(input())
arry = list(map(int, sys.stdin.readline().split()))

summ = [0] * (n+1)

for i in range(n):
    ary = arry[::]
    # print(arry, '*')
    # print(ary, '&')
    if i == 0:
        ary[i+1] = 0

    elif i == n-1:
        ary[i-1] = 0
    else:
        ary[i-1] = 0
        ary[i+1] = 0
    if int(ary.index(max(ary))) == i:
        maxx = ary[i]
        ary[i] = 0
        summ[i] = maxx + max(ary)
    else:
        summ[i] = max(ary) + ary[i]
    # print(ary)
    print(summ)
