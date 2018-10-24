import random
from cal_time import *


def sift(li, low, high):
    tmp = li[low]
    i = low
    j = 2 * i + 1
    while j <= high:    # 第一个退出条件：j不存在
        if j + 1 <= high and li[j+1] > li[j]:   # 如果右孩子存在并且右孩子比左孩子大
            j += 1  # j指向右孩子
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:   # 第二个退出条件：j位置的值比tmp小
            break
    li[i] = tmp

@cal_time
def heap_sort(li):
    # 1. 建堆
    n = len(li)
    for i in range(n//2-1, -1, -1): # i表示遍历的low
        sift(li, i, n-1)    # low:i high:统一写成最后一个位置对正确性没有影响
    # 2. 挨个出数：退休 棋子 调整
    for i in range(n-1, 0, -1):    # i 表示当前位置堆的high
        li[i], li[0] = li[0], li[i]
        sift(li, 0, i-1)
        # print(li)


li = list(range(100000))
random.shuffle(li)
# print(li)
heap_sort(li)


