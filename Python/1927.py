import heapq
import sys
input=sys.stdin.readline

itera = int(input())
lst=[]
cnt=0
for _ in range(itera) :
    number=int(input())
    if cnt== 0 and number==0:
        print(0)
    elif number==0 :
        print(heapq.heappop(lst))
        if cnt>0 :
            cnt-=1
    else :
        heapq.heappush(lst,number)
        cnt+=1
                 
    # print(f'dq={dq}')

