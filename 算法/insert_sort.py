import random
from cal_time import *

@cal_time
def insert_sort(li):
    for i in range(1, len(li)):
        # i 表示趟数 还表示摸到牌的位置
        j = i - 1
        tmp = li[i]
        while j >= 0 and li[j] > tmp:
            # 两个终止条件： 1. j==-1 2. j位置的值小于等于tmp
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp
        # print(li)

li = list(range(10000))
# random.shuffle(li)
#print(li)
insert_sort(li)