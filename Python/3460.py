
a= int(input())


for _ in range(a) :
    b= bin(int(input()))
    for i in range(len(b)) :
        if b[-i]=='1' :
            print(f'{i-1}',end=' ')

