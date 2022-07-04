num= int(input())
for _ in range(num) :

    a,b= input().split()
    print('Distances: ',end='')
    for i in range(len(a)) :
        if ord(b[i])>=ord(a[i]) :
            print(f'{abs(ord(b[i])-ord(a[i]))} ',end='')
        elif ord(b[i])<ord(a[i]) :
            print(f'{abs((ord(b[i])+26)-ord(a[i]))} ',end='')
    print()


