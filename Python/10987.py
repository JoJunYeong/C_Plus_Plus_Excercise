a=list(input())
cnt=0
for i in range(len(a)) :
    if a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u' :
        cnt+=1
print(cnt)