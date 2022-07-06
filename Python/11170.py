a=int(input())

for _ in range(a) :
    b,c = map(int,input().split())
    cnt=0
    for i in range(b,c+1) :
        i = str(i)
        cnt+=i.count('0')
    print(cnt)