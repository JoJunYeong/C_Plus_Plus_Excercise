a= int(input())
i=666 
cnt=0
while True :
    if str(i).find('666')!=-1 :
        cnt+=1
    if cnt==a :
        print(i)
        break
    i+=1



