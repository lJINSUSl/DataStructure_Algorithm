# def solution(phone_book):
#     answer = True
#
#     for i in range(len(phone_book)):
#         rest = phone_book[::]
#         rest.remove(rest[i])
#
#         for j in range(len(rest)):
#             if phone_book[i] == rest[j][:len(phone_book[i])]:
#                 answer = False
#     return answer
#
# print(solution(["119", "97674223", "1195524421"]))+

import collections
from itertools import combinations

# def solution(clothes):
#     answer = 1
#
#     clothes = [i[1] for i in clothes]
#     clothes.sort()
#
#     dictt = collections.Counter(clothes)
#     dic = dictt.most_common()
#
#     ls = [i[1] for i in dic]
#
#
#     for i in ls:
#         answer = answer * (i+1)
#     answer -= 1
#
#     return answer
#
# print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"],["green_turban", "headgr"],["green_turban", "headgr"],["green_turban", "headgr"]]))

# def solution(genres, plays):
#     dictt = []
#     for i in range(len(genres)):
#         dictt.append((genres[i],plays[i]))
#     print(dictt)
#     dic = collections.Counter(dictt)
#     num = dic.most_common()
#     print(num)
#
#     answer = []
#     return answer
#
# solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500])

def solution(progresses, speeds):
    answer = []
    plus = []
    num = 0
    nu = len(progresses)
    while sum(answer) < nu:
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]

        print(progresses)
        while progresses[0] >= 100:
            num += 1
            progresses.pop(0)
            speeds.pop(0)
        print(progresses)

        if num > 0:
            answer.append(num)
            num = 0
        print(answer, sum(answer), len(speeds))

    return answer

print(solution([93,30,35],[1,30,5]))