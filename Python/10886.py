a=int(input())
lst = list(int(input()) for _ in range(a))

cnt,cnt2=0,0

for i in range(a) :
    if lst[i] == 0 :
        cnt+=1
    else :
        cnt2+=1

if cnt>cnt2 :
    print('Junhee is not cute!')
else :
    print('Junhee is cute!')