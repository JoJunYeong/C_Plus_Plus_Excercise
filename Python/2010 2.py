import sys


# 이 문제는 이걸 쓰느냐 안쓰느냐 문제이다. 로직은 매우 간단하다.
# input에 관한 시간초과 문제이다.
input = sys.stdin.readline  

a= int(input())
c=0
for i in range(a) :
    b=int(input())
    c+=b

print(c-(a-1))


