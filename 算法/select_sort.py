import random
from cal_time import *

def find_min_pos(li):
    min_pos = 0
    for i in range(1, len(li)):
        if li[i] < li[min_pos]:
            min_pos = i
    return min_pos

@cal_time
def select_sort(li):
    for i in range(len(li)-1):
        # i 表示第i趟 无序区的范围 i ~ n-1
        min_pos = i # 默认最小值是无序区第一个数
        for j in range(i+1, len(li)):
            if li[j] < li[min_pos]:
                min_pos = j
        li[i], li[min_pos] = li[min_pos], li[i]
        # print(li)

li = list(range(10000))
#random.shuffle(li)
#print(li)
select_sort(li)

