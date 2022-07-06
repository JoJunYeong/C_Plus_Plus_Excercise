
from collections import deque
import sys

input=sys.stdin.readline

dq= deque()

node, line = map(int, input().split())

for i in range(node+2) :
    dq.append([])

# print(dq)

for i in range(line) :
    node1,node2 = map(int, input().split())
    dq[node1] += [node2]
    dq[node2] += [node1]

# print(dq)
cnt=0
visit=deque()
result=[]
for i in range(1,node+1) :
    if len(dq[i]) == 0 and i not in result:
        cnt+=1
        continue
    if i not in result:
        visit += dq[i]
        # result.append(visit[0])
        # print(f'i={i}, visit={visit}, result={result}')
        cnt+=1
        while len(visit)!=0 :
            # print('반복')
            if len(visit) == 0 :
                break
            tmp=visit.popleft()
            if tmp not in result :
                result.append(tmp)
                visit+=dq[tmp]
                # print(f'{visit}+={dq[tmp]}')
            # print(visit)
            
    

print(cnt)










