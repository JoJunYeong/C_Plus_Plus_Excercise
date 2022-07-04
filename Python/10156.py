a,b,c = map(int, input().split())

a = a*b-c
if a<=0:
    a=0

print(a)