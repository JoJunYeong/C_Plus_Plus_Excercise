a= int(input())

lst = list(map(int,input().split()))

lst2=[]
for i in range(1,1000) :
    cnt=0
    for j in range(1,i+1) :
        if i%j==0 :
            cnt+=1
    if cnt==2 :
        lst2.append(i)
cnt=0
for i in range(len(lst)) :
    if lst[i] in lst2 :
        cnt+=1

print(cnt)