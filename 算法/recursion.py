#
# def print_str(n):
#     if n > 0:
#         print("抱着",end='')
#         print_str(n-1)
#         print("的我",end='')
#     else:
#         print("我的小鲤鱼", end='')
#
# print_str(5)

# 1 1 2 3 5 8 13

# def f(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return f(n-1) + f(n-2)
# #
def f(n):
    li = [0,1,1]
    if n <= 2:
        return li[n]
    for i in range(3, n+1):
        li.append(li[-1] + li[-2])
    return li[n]

"""
n层台阶有f(n)种走法

1. 最后一步走1层
    f(n-1)
2. 最后一步走2层
    f(n-2)

f(n) = f(n-1) + f(n-2)
f(1) = 1
f(2) = 2
"""



print(f(4))