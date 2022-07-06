a=int(input())
lst=list(list(map(int, input().split())) for _ in range(a))
s1,s2=100,100

for i in range(a) :
    if lst[i][0] > lst[i][1] :
        s2-=lst[i][0]
    elif lst[i][0] < lst[i][1] :
        s1-=lst[i][1]

print(s1,s2)
