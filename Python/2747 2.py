a= int(input())
lst=[]

for i in range(a+1) :
    if i==0 :
        lst.append(i)
        continue
    elif i==1 :
        lst.append(i)
        continue
    else :
        lst.append(lst[i-2]+lst[i-1])

print(lst[-1])