a,b=map(int,input().split())
lst = list(map(int,input().split()))
lst2=[]
for i in range(a) :
    if lst[i]<b :
        lst2.append(str(lst[i]))
print(' '.join(lst2))



