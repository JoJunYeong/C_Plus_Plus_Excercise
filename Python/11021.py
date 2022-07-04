iteration = input()
iteration = int(iteration)


a=list( input().split() for _ in range(iteration) )


for i in range(iteration) :
    b=int(a[i][0])+int(a[i][1])
    print("Case #"+str(i+1)+": "+str(b))