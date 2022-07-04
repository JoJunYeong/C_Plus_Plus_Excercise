import sys
from collections import deque

input=sys.stdin.readline

number, target = map(int,input().split())

wait_queue = deque()
wait_queue.append([number,0])
calcul_cnt=0
while True :
    calcul_cnt+=1
    number, cnt = wait_queue.popleft()

    # print(f'연산{calcul_cnt}번, number={number}, cnt={cnt}, wait_queue={wait_queue}\n')
    if number > target :
        print(cnt+(number-target))
        break
    if number == target :
        print(cnt)
        break
    if number+1 == target or number-1 == target or number*2 == target :
        print(cnt+1)
        break
    cnt+=1
    
    wait_queue.append([number+1,cnt])
    wait_queue.append([number-1,cnt])
    wait_queue.append([number*2,cnt])



