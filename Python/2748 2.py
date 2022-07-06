a = int(input())

lst=[0]

# 피보나치 
for i in range(1,a+1) :
    if i==1 :
        lst.append(1)
    else :
        lst.append(lst[i-2] + lst[i-1])

print(lst[-1])