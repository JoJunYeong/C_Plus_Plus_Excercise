a = int(input())

for i in range(1,a+1) :
    print('*'*i+' '*((a*2)-(2*i))+'*'*i)

for i in range(a-1,0,-1) :
    print('*'*i+' '*((a*2)-(2*i))+'*'*i)


