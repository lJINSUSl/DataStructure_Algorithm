##입력##
# 3
# 15
# 21
# 27


import sys
n = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for _ in range(n)]
sorted(array, reverse=True)
print(array)


