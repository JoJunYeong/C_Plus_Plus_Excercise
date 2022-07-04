num=int(input())

for i in range(num) :
    up=0
    right=1
    a,b,c = map(int,input().split())
    for j in range(c) :
        if up == a :
            up=1 
            right+=1
        else :
            up+=1
        # print(f'{up}{right:02d}')
    # print(f'right={right}')

    print(f'{up}{right:02d}')

    
   
