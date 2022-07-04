a,b = map(int,input().split())
result=1
result2=1
bb=b
aa=a
while True :
    if a==1 or b==0 :
        result=1
        break
    if aa==(a-b) :
        break
    result *= aa
    aa-=1
    result2 *= bb
    bb-=1

print(int(result/result2))




