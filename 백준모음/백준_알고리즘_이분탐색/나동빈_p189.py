##입력##
# 1 2 4 6 8 9

import sys
n, t = map(int, sys.stdin.readline().split())
ary = list(map(int,sys.stdin.readline().split()))

def binary_search(array, target, start, end): #start,end는 리스트 인덱스, target은 숫자
    mid = (start + end) //2
    if array[mid] == target:
        return mid

    if array[mid] > target:
        end = mid - 1
        binary_search(array,target, start, end)
    elif array[mid] < target:
        start = mid + 1
        binary_search(array, target, start, end)

result = binary_search(ary,t,0,n-1)

if not result:
    print("원소가 존재하지 않습니다")
else:
    print(result + 1)

