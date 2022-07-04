a=int(input())

for _ in range(a) :
    b= int(input())
    sum_c,sum_d = 0,0
    for i in range(b) :
        c,d=map(float,input().split())
        sum_c+=c
        sum_d+=(d*c)
    print(int(sum_c),f'{sum_d/sum_c :.01f}')