from math import gcd

a=int(input())
lst =  list(input().split() for _ in range(a))

for i in range(a) :
    print(int(int(lst[i][0])*int(lst[i][1])/gcd(int(lst[i][0]),int(lst[i][1]))))






