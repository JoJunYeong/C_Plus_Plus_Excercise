from collections import defaultdict

a= int(input())
dic = defaultdict()
lst=list(map(int, input().split()))
for i in range(a) :
    # print(f'lst[{i}]={lst[i]}')
    if lst[i] not in dic :
        dic[lst[i]]=1
    else :
        dic[lst[i]]+=1

b= int(input())
lst2=list(map(int, input().split()))
for i in range(b) :
    if lst2[i] in dic :
        print(dic[lst2[i]],'',end='')
    else :
        print(0,'',end='')








