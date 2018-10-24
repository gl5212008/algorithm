import random
from cal_time import *
# def merge_two_list(li1, li2):
#     i = 0
#     j = 0
#     ans = []
#     while i < len(li1) and j < len(li2):
#         if li1[i] < li2[j]:
#             ans.append(li1[i])
#             i += 1
#         else:
#             ans.append(li2[j])
#             j += 1
#     while i < len(li1):
#         ans.append(li1[i])
#         i += 1
#     while j < len(li2):
#         ans.append(li2[j])
#         j += 1
#     return ans


def merge(li, low, mid, high):
    i = low
    j = mid + 1
    li_tmp = []
    while i <= mid and j <= high:   # 如果两边都有数
        if li[i] < li[j]:
            li_tmp.append(li[i])
            i += 1
        else:
            li_tmp.append(li[j])
            j += 1
    while i <= mid:
        li_tmp.append(li[i])
        i += 1
    while j <= high:
        li_tmp.append(li[j])
        j += 1
    for i in range(len(li_tmp)):
        li[low+i] = li_tmp[i]


def _merge_sort(li, low, high):
    if low < high:  # 至少两个元素
        mid = (low + high) // 2
        _merge_sort(li, low, mid)
        _merge_sort(li, mid+1, high)
        # print(li[low:mid + 1], li[mid + 1:high + 1])
        merge(li, low, mid, high)
        # print(li[low:high+1])


@cal_time
def merge_sort(li):
    _merge_sort(li, 0, len(li)-1)


li = [10,4,6,3,8,2,5,7]
# random.shuffle(li)
merge_sort(li)


