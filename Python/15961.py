import sys
from collections import deque

input=sys.stdin.readline

n,d,k,c = map(int,input().split())
chobab = deque()
chobab_front=deque()
maxx=0
dic={}
passs=False
for i in range(n) :
    number = int(input())
    if i >= k :
        tmp=chobab.popleft()
        if dic[tmp] > 1 :
            dic[tmp]-=1
        else :
            del dic[tmp]
    
    if i <= k :
        chobab_front.append(number)

    chobab.append(number)

    if number not in dic :
        dic[number] = 1
    else :
        dic[number]+=1
    
    tmp_len=len(dic)
    if c not in dic :
        maxx=max(maxx, tmp_len + 1 )
    else :
        maxx=max(maxx, tmp_len )

    if maxx == k+1 :
        passs=True
        break


if ~passs :
    for i in range(k) :
        number = chobab_front.popleft()
        tmp=chobab.popleft()

        if dic[tmp] > 1 :
                dic[tmp]-=1
        else :
            del dic[tmp]

        if number not in dic :
            dic[number] = 1
        else :
            dic[number]+=1
        
        tmp_len=len(dic)
        if c not in dic :
            maxx=max(maxx, tmp_len + 1 )
        else :
            maxx=max(maxx, tmp_len )

        if maxx == k+1 :
            break

print(maxx)
    