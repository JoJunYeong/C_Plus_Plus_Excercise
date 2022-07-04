from collections import deque

a=int(input())

weight_lst=[]
height_lst=[]
dq = deque()

for i in range(a) :
    
    weight, height = map(int, input().split())
    weight_lst.append(weight)
    height_lst.append(height)
    dq.append([weight,height])
    
for i in range(a) :
    w,h=dq.popleft()
    rank=1
    for j in range(a) :
        if w>weight_lst[j] and h>height_lst[j] :
            continue
        elif w>weight_lst[j] or h>height_lst[j] :
            continue
        elif w<weight_lst[j] and h<height_lst[j] :
            rank+=1
    print(rank,'',end='')