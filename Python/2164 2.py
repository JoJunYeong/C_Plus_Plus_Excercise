from collections import deque

a=int(input())
dq=deque(i for i in range(1,a+1))

for i in range(a-1) :
    dq.popleft()
    tmp = dq.popleft()
    dq.append(tmp)
print(dq[0])


