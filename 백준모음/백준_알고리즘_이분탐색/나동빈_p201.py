import sys
n,m = map(int, sys.stdin.readline().split())
duck = list(map(int, sys.stdin.readline().split()))
duck = sorted(duck)

# def binary_search(array, target, start, end):
#     mid = (start+end)//2
#
#     summ = [(i - array[mid]) for i in array if (i-array[mid])>0]
#     num_sum = sum(summ)
#     if start >= end:
#         return None
#     elif num_sum == target:
#         return array[mid]
#
#     elif num_sum < target:
#         return binary_search(array, target, start, mid - 1)
#     elif num_sum > target:
#         return binary_search(array,target,mid + 1, end)
#
# result = binary_search(duck,m,0,n-1)
# print(result)
start = 0
end = max(duck)
result = 0
while (start <= end):
    mid = (start + end) // 2
    summ = [(i - mid) for i in duck if (i - mid) > 0]
    num_sum = sum(summ)

    if num_sum < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)