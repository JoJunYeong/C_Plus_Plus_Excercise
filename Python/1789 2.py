sum = int(input())
count=0

for i in range(1,sum) :
    if (sum - i)>i :
        sum = sum-i
        count=count+1
        # print('sum=',sum,'i=',i,'count=',count)
    else :
        count = count+1
        break

print(count)


