import sys

n,k = map(int, sys.stdin.readline().split())
MOD = 10007
sys.setrecursionlimit(10 ** 7)


# cache = [[-1,-1]] * 1000
cache = [[0] * 3 for _ in range(4)]
print(cache)
def combination(n,k):
    if k==0 or k==n:
        cache[n][k] = 1
    else:
        cache[n][k] = combination(n-1,k-1) + combination(n-1,k)
    print(cache)
    return cache[n][k]

# print(cache)
print(combination(n,k))