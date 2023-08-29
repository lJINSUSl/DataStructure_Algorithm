import sys

n = int(sys.stdin.readline())
array = []
for _ in range(n):
    dicta = sys.stdin.readline().split()
    array.append((dicta[0],int(dicta[1])))
array = dict(array)
array = sorted(array, key=lambda item: item[1])


for i in array:
    print(i, end=' ')