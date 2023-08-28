loc = input()

x,y = int(ord(loc[0])) -96, int(loc[1])

print(x,y)

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [1,-1,2,-2,2,-2,1,-1]

cnt = 0

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    else:
        cnt += 1

print(cnt)