from collections import deque

num = int(input())

for i in range(num) :
    total, numbering = map(int, input().split())
    dq=deque(map(int,input().split()))
    target=dq[numbering]
    cnt=0
    maxx=max(dq)
    while True :
        # print(dq)
        if dq[0] != maxx :
            # print('enter')
            tmp=dq.popleft()
            dq.append(tmp)
            if numbering == 0 :
                numbering = len(dq)-1
            else :
                numbering-=1
        elif dq[0] == maxx :
            # print(f'enter2, target={numbering}')
            cnt+=1
            dq.popleft()
            if numbering == 0 :
                print(cnt)
                break
            maxx=max(dq)
            numbering-=1
        


