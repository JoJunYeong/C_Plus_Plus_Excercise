
a=int(input())
string=input()
summ=0
for i in range(a) :
    summ+=(ord(string[i])-96)*(31**i)
print(summ % 1234567891)

