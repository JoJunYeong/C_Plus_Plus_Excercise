import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n=1000000
# 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
sieve = [True] * (n+1)
sosu = []
# n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
m = int(n ** 0.5)
for i in range(2, n+1):
    if sieve[i] == True:           # i가 소수인 경우
        sosu.append(i)
        for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
            sieve[j] = False


num = []
while True:
    b = input()
    b=int(b)
    if b==0:
        break
    for i in range(3,b) :
        if (sieve[i]==True and sieve[b-i]==True) :
            print( str(b) +" = "+str(i)+" + "+str(b-i))
            break
    
 



# for k in range(len(num)):   
#     for i in range(len(sosu)) :
#         asd = 0
#         for j in range(len(sosu)) :
#             if ((sosu[i]+sosu[j])==num[k]) :
#                 print( str(num[k]) +" = "+str(sosu[i])+" + "+str(sosu[j]))
#                 asd=1
#                 break
#         if asd==1 :
#             break   







