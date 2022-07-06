from collections import defaultdict
import operator

a = int(input())
dic=defaultdict()
lst=list(map(int,input().split()))
for i in range(a) :
    dic[i+1]=lst[i]
sort = sorted(dic.items(), key=operator.itemgetter(1) )
sum,cnt=0,0
for i in range(a) :
    cnt += sort[i][1]
    sum += cnt
print(sum)


