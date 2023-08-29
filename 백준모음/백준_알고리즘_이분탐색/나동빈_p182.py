import sys

N, K = map(int, sys.stdin.readline().split())
list1 = list(map(int, sys.stdin.readline().split()))
list2 = list(map(int, sys.stdin.readline().split()))

list1 = sorted(list1)
list2 = sorted(list2,reverse=True)

for _ in range(K):
    list1[_] = list2[_]

print(sum(list1))