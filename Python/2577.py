from collections import defaultdict

a=int(input())
b=int(input())
c=int(input())
dic =defaultdict()
sum = str(a*b*c)

for i in range(len(sum)) :
    # print(f'sum[{i}:{i+1}]={sum[i:i+1]}')
    if int(sum[i:i+1]) not in dic :
        dic[int(sum[i:i+1])]=1
    else :
        dic[int(sum[i:i+1])]+=1
for i in range(10) :
    if i in dic :
        print(dic[i])
    else :
        print(0)