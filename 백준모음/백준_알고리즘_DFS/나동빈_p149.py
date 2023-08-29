import sys
N,M = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
print(graph)

def dfs(x,y):
    pass