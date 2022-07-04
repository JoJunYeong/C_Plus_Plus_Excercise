a= int(input())
lst=['*']*a
for i in range(1,a+1) :
    if i%2==1 :
        print(' '.join(lst))
    else :
        print(' '+' '.join(lst))
    