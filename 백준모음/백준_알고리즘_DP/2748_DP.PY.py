import sys

#memoization을 위한 캐시(저장소) 설정
cache = [-1] * 91
cache[0] = 0
cache[1] = 1


def f(n):
    if cache[n] == -1:
        cache[n] = f(n - 1) + f(n - 2)

    return cache[n]

print(f(int(sys.stdin.readline())))