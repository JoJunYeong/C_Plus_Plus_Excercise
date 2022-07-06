from collections import defaultdict,deque

a1= int(input())
lst1=list(map(int, list(input().split())))
a2= int(input())
dic=defaultdict()
dq=deque()
dq.extend(list(map(int, list(input().split()))))
for i in lst1 :
    dic[i]=0
for i in range(a2) :
    q= dq.popleft()
    if q not in dic :
        print(0)
    else :
        print(1)
