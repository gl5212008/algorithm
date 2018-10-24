import random
from cal_time import *

@cal_time
def bubble_sort(li):
    for i in range(len(li)-1):  # i表示第i趟,共n-1趟
        # 第i趟 无序区范围 0~n-i-1
        for j in range(len(li)-i-1): # j表示箭头
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
        # print(li)

@cal_time
def bubble_sort_2(li):
    for i in range(len(li)-1):  # i表示第i趟,共n-1趟
        # 第i趟 无序区范围 0~n-i-1
        exchange = False
        for j in range(len(li)-i-1): # j表示箭头
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        if not exchange:
            return
        # print(li)


#li = [8,5,7,9,4,2,6,1,3]
li = list(range(10000))
random.shuffle(li)
bubble_sort_2(li)
#print(li)
