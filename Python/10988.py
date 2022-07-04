a= input()
b=1
c=a[::-1]
for i in range(int(len(a)/2)) :

    if a[i:i+1] == c[i:i+1] :
        continue
    else :
        b=0
        break
print(b)