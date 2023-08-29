x = int(input())

d = [0] * 300001

d[1] = 0
start = 0

def mak1(xx):
    if xx==1:
        return 0
    elif xx == 2 or xx==3, xx==5:
        return 1
    if d[xx] !=0:
        return d[xx]
    d[xx+1]


for i in range(1,30001):
    mak1(i)
print(d[x])

