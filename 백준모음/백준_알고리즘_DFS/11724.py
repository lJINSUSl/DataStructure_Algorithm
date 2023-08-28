import sys


N, M = map(int,sys.stdin.readline().split())


adj = [[0] *N for _ in range(N)]

for _ in range(M):
    node1, node2 = map(int,sys.stdin.readline().split())
    node1 -= 1
    node2 -= 1
    adj[node1][node2] = adj[node2][node1] = 1
# print(adj)
#
# for row in adj:
#     print(row)

ans = 0
chk = [False] * N
# print(chk)

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True

            dfs(nxt)
    # print(chk)

for i in range(N):
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i)

print(ans)