a,b = map(int,input().split())

lst2 = list(int(input()) for _ in range(a))
lst2.reverse()
# print(lst2)
cnt=0
for i in lst2 :
    if int(b/i) > 0 :
        cnt += int(b/i)
        b%=i
        if b==0 :
            break

print(cnt)