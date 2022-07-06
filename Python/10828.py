from collections import deque
import sys

input=sys.stdin.readline

a= int(input())
dq=deque()

for i in range(a) :
    lst= input().split()
    if lst[0]=='push' :
        dq.append(int(lst[1]))
    elif lst[0]=='pop' :
        if len(dq)>0 :
            print(dq.pop())
        else :
            print(-1)
    elif lst[0]=='size' :
        print(len(dq))
    elif lst[0]=='empty' :
        if len(dq)>0 :
            print(0)
        else :
            print(1)
    elif lst[0]=='top' :
        if len(dq)>0 :
            print(dq[-1])
        else :
            print(-1)
