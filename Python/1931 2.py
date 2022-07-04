import sys

input = sys.stdin.readline

num = int(input())
lst=list(list(map(int,input().split())) for _ in range(num))
lst.sort(key = lambda x:[x[0],x[1]])
# print(lst)
cnt=1
start, end=lst[0][0], lst[0][1]
for i in range(1,num) :
    if lst[i][0]>=end : 
        # print(f'만료교체 [{start}, {end}] => lst[{i}]={lst[i]}')
        start=lst[i][0] 
        end=lst[i][1]
        cnt+=1
        
    elif end>=lst[i][1] :
        # print(f'end가 더 짧아서 교체 [{start}, {end}] => lst[{i}]={lst[i]}')
        end=lst[i][1]
        start=lst[i][0]
        
print(cnt)
    

