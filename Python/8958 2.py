num=int(input())
for _ in range(num) :
    a=input()
    cnt,sum=0,0
    for i in range(len(a)) :
        if a[i:i+1] =='O' :
            cnt+=1
            sum+=cnt
        else :
            cnt=0
    print(sum)