lst = list(input().split() for _ in range(3))

for i in range(2) :
    a,b,cnt,cnt2=0,0,0,0
    for j in range(3) :
        if j==0 or a==int(lst[j][i]) :
            a= int(lst[j][i])
            cnt+=1
        elif int(lst[j][i]) !=a :
            b= int(lst[j][i])
            cnt2+=1
    if cnt==1 :
        print(a,'',end='')
    elif cnt2==1 :
        print(b,'',end='')