import sys

N, M = map(int, sys.stdin.readline().split())

mat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

small_num = []

print(mat)

for n in range(len(mat)):
    small_num.append(min(mat[n]))
    print(small_num)
print(small_num)

print(max(small_num))