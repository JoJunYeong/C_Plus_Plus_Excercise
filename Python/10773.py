a=int(input())

lst=[]

for i in range(a) :
    b= int(input())
    if b==0 :
        del lst[-1]
    else :
        lst.append(b)

print(sum(lst))




