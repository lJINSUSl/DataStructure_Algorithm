import sys

n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_list = list(map(int,sys.stdin.readline().split()))

m_li = ['no'] * m



# for mm in range(len(m_list)):
#     for nn in range(len(n_list)):
#         if m_list[mm] == n_list[nn]:
#
#             m_li[mm] = 'yes'
#
# for m in m_li:
#     print(m, end=' ')
############################## 이진 트리로 문제풀기 ##################################

n_list = sorted(n_list)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    if array[mid] == target:
        return mid

    elif array[mid] > target:
        end = mid - 1
        return binary_search(array,target, start, end)

    elif array[mid] < target:
        start = mid + 1

        return binary_search(array, target, start, end)

for m in range(len(m_list)):
    result = binary_search(n_list,m_list[m],0,n-1)

    if result == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')
