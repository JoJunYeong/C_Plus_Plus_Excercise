import sys
from collections import deque

input=sys.stdin.readline

dq=deque()
a,b=map(int,input().split())

for i in range(1,a+1) :
    dq.append(i)
print(f'<',end='')
for i in range(a) :
    for j in range(b-1) :
        dq.append(dq.popleft())
    print(f'{dq.popleft()}',end='')
    if i != a-1 :
        print(', ',end='')
print(f'>',end='')

