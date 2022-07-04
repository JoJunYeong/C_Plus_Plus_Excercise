
from itertools import combinations
import sys
input=sys.stdin.readline
a=int(input())

for i in range(a) :
    lst=[]
    number=int(input())
    lst2=[]
    for j in range(number) :
        a,b = input().split()
        if b not in lst :
            lst.append(b)
            lst2.append(1)
        else :
            lst2[lst.index(b)]+=1

    # print(f'lst2={lst2}')
    if len(lst2)== 0:
        print(0)
    else :
        summ=0
        tmp=1
        for i in range(len(lst2)):
            tmp*=(lst2[i]+1)
        tmp-=1
        
        print(f'{tmp}')

            

