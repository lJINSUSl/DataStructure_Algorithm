import sys

N = int(input())
mat = [[0] * N for _ in range(N)]

walk = sys.stdin.readline().split()

wid = 1
height = 1
for w in walk: # len(range(walk)) 가 아니라 walk가 들어가야 함.
    if w == "R":
        if wid < 5:
            wid += 1

    elif w == 'L':
        if wid > 1:
            wid -= 1

    elif w == 'U':
        if height > 1:
            height -= 1

    elif w == 'D':
        if height < 5:
            height += 1



print(height, wid)

############################## 정답답안 ####################################

n = int(input())
x, y = 1, 1
plans = input().split()
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx <1 or ny <1 or nx > n or ny > n:
        continue

    x,y = nx,ny
print(x,y)