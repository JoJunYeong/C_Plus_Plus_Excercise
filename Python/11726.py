
import sys
input=sys.stdin.readline


a=int(input())
lst=[]
lst.append(1)
lst.append(2)
if a==1 :
    print(1)
elif a==2 :
    print(2)
else :
    for i in range(2,a) :
        lst.append(lst[i-1]+lst[i-2])
        # print(f'lst={lst}')
    print(lst[-1]%10007)
