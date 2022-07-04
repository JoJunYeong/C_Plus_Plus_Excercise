#숫자 입력받기
a,b = map(int, input().split())
c=1

#최대공약수
i=2
while True :
    if min(a,b) < i :
        break
    if a%i==0 and b%i==0 :
        a //= i
        b //= i
        c *= i
        i=1
    i+=1
print(c)

#최소공배수
print(c*a*b)






