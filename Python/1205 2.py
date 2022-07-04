count2=1
a,score,count =map(int,input().split())
if a==0 :
    lst = [0]
else :
    lst = list(map(int,input().split()))
    for i in range(0,a) :
        if score<lst[i] :
            count2 = count2+1
        elif score>lst[i] :
            break
        if i==count-1 :
            if score<=lst[i] :
                count2=-1





        
    # print("\nlst[i]=",str(lst[i]))
    # print("i=",str(i))
    # print("count2=",str(count2))


    
print(count2)