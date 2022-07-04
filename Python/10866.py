from collections import deque
import sys

input=sys.stdin.readline

a= int(input())
dq=deque()

for i in range(a) :
    lst= input().split()
    if lst[0]=='push_front' :
        dq.appendleft(int(lst[1]))
    elif lst[0]=='push_back' :
        dq.append(int(lst[1]))
    elif lst[0]=='pop_front' :
        if len(dq)>0 :
            print(dq.popleft())
        else :
            print(-1)
    elif lst[0]=='pop_back' :
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
    elif lst[0]=='front' :
        if len(dq)>0 :
            print(dq[0])
        else :
            print(-1)
    elif lst[0]=='back' :
        if len(dq)>0 :
            print(dq[-1])
        else :
            print(-1)
