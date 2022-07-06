a=int(input())
b=int(input())

lst=[]
for i in range(min(a,b),max(a,b)+1) :
    cnt=0
    for j in range(1,i+1) :
        if i%j==0 :
            cnt+=1
    if cnt==2 :
        lst.append(i)
if len(lst)==0 :
    print(-1)
else :
    print(sum(lst))
    print(min(lst))

