import sys
import random
from cal_time import *

sys.setrecursionlimit(10000)

def partition(li, left, right):
    i = random.randint(left, right)
    li[left], li[i] = li[i], li[left]

    tmp = li[left]
    while left < right:
        # 从右边找比tmp小的数
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        # 从左边找比tmp大的数
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left


def _quick_sort(li, left, right):
    if left < right:    # 表示至少两个元素
        mid = partition(li, left, right)
        _quick_sort(li, left, mid-1)
        _quick_sort(li, mid+1, right)

@cal_time
def quick_sort(li):
    _quick_sort(li, 0, len(li)-1)

# @cal_time
# def sys_sort(li):
#     li.sort()


li = list(range(100000))
random.shuffle(li)
quick_sort(li)