# from collections import defaultdict
# import operator
# a= int(input())
# for i in range(a) :
#     num = int(input())
#     dic = defaultdict()
#     for j in range(num) :
#         nu=num
#         q,w = map(int,input().split())
#         dic[q]=w
#     sort = sorted(dic.items(), key=operator.itemgetter(1))
#     sort2 = sorted(dic.items(), key=operator.itemgetter(0))
#     # print('sort=',sort)
#     # print('sort2=',sort2)
#     for j in sort :
#         for k in range(sort.index(j)) :
#             # print('k=',k, 'j=',j,'sort.index(j)=',sort.index(j))
#             if sort[k] in sort2 :
#                 s2_ind = sort2.index(sort[k])
#                 if s2_ind < sort2.index(j) :
#                     # print('nu=',nu,'sort1=',sort[k],'sort2.index(j)=',sort2.index(j),'sort2=',sort[sort2.index(j)])
#                     nu-=1
#                     break
#     print(nu)
import sys
from collections import defaultdict
import operator
input=sys.stdin.readline
a= int(input())
for i in range(a) :
    num = int(input())
    dic = defaultdict()
    for j in range(num) :
        nu=num
        q,w = map(int,input().split())
        dic[q]=w
    sort = sorted(dic.items(), key=operator.itemgetter(0))
    x=sort[0][1]
    cnt=1
    for z in range(1,num) :
        if x>sort[z][1] :
            x=sort[z][1]
            cnt+=1
    print(cnt)






