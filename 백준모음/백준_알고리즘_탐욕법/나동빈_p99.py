import sys

N, K = map(int,sys.stdin.readline().split())

cnt = 0

while N>1:
    if N % K==0:
        N = int(N / K)

        cnt += 1
        print(N, cnt, '2')
    else:
        N = N-1
        cnt += 1
        print(N,cnt,'1')

print(cnt)