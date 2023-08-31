x = int(input())

d = [0] * 300001

d[1] = 0
start = 0

# def mak1(xx):
#     if xx==1:
#         return 0
#     elif xx == 2 or xx==3, xx==5:
#         return 1
#     if d[xx] !=0:
#         return d[xx]
#     d[xx+1]
#
#
# for i in range(1,30001):
#     mak1(i)
# print(d[x])

for i in range(2,x+1):
    if d[i] != 0:
        continue
    else:
        minus_one = d[i-1] + 1
        div_two, div_three, div_five = 999999,999999,999999
        if i % 2 == 0:
            div_two = d[i//2] +1
        if i % 3 == 0:
            div_three = d[i // 3] + 1
        if i % 5 == 0:
            div_five = d[i // 5] + 1
        d[i] = min(minus_one,div_two,div_five,div_three)

print(d[x])

