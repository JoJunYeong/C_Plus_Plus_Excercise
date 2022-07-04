a= int(input())
cnt1,cnt2,cnt3=0,0,0
while True :
    if a%300 ==0 :
        cnt1+=1
        a=int(a-300)
        if a==0 :
            print(cnt1,cnt2,cnt3)
            break
    elif a%60==0 :
        cnt2+=1
        a=int(a-60)
        if a==0 :
            print(cnt1,cnt2,cnt3)
            break
    elif a%10==0 :
        cnt3+=1
        a=int(a-10)
        if a==0 :
            print(cnt1,cnt2,cnt3)
            break
    else :
        print(-1)
        break

