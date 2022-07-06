import sys
from collections import defaultdict

input = sys.stdin.readline

dic=defaultdict()
number_count = int(input())

original_lst = list(map(int,input().split()))
lst_set = list(set(original_lst))
lst_sorted = sorted(lst_set, key=lambda x:x,reverse=False)

for i in range(len(lst_sorted)) :
    dic[lst_sorted[i]]=i

for i in original_lst :
    print(dic[i],end=' ')

