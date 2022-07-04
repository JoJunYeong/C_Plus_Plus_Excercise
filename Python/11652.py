import sys
from collections import defaultdict
import operator

input=sys.stdin.readline
n = int(input())
dic = {}

for case in range(n):
    tmp = int(input())
    if tmp in dic:
        dic[tmp] += 1
    else:
        dic[tmp] = 1

# sort = sorted(dic.items(), key=operator.itemgetter(0))
sort = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(sort[0][0])

