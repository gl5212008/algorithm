import heapq
import random
# queue

# 优先队列

# li = [5,7,8,9,4,1,6,2,3]
# heapq.heapify(li)
# print(li)
#
# heapq.heappush(li, 0)
# print(li)
#
# val = heapq.heappop(li)
# print(val)

li = list(range(10000))
random.shuffle(li)


print(heapq.nsmallest(10, li))
