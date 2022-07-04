a=input()
sum =10
tmp=a[0:1]
for i in range(1,len(a)) :
    # print('tmp=',tmp,'a[i:i+1]=',a[i:i+1])
    if tmp == a[i:i+1] :
        sum+=5
    else :
        sum+=10
        tmp = a[i:i+1]
    # print('sum=',sum)
print(sum)