while True :
    a= int(input())
    lst=[]
    lst.append(1)
    if a==-1:
        break
    print(a,'',end='')
    for i in range(2,int(a/2)+1) :
        if a%i==0 :
            lst.append(i)
    if sum(lst)==a :
        print('= ',' + '.join(str(i) for i in lst),sep='')
    else :
        print('is NOT perfect.')
