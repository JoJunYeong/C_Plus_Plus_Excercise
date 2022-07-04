lst=[]
for _ in range(7) :
    b=int(input())
    if b%2==1 :
        lst.append(b)

if len(lst) == 0 :
    print(-1)
else :
    print(sum(lst))
    print(min(lst))