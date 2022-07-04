a,b = map(int,input().split())
count=0
sum=0

for i in range(1,b+1):
    for j in range(1,i+1):
        count = count+1
        if count>b :
            break
        elif count>=a :
            # print("count=",str(count)+" sum=",str(sum)+" a=",str(a)+" b=",str(b)+" i=",str(i)+" j=",str(j))
            sum=i+sum

print(sum)