a= int(input())
apartment=[[0]*16 for _ in range(17)]
for i in range(1,16) :
    for j in range(1,15) :
        if j==1 :
            apartment[i][j]=1
        elif i==1 :
            apartment[i][j]=j
        else :
            apartment[i][j] = apartment[i][j-1] + apartment[i-1][j]
# for i in range(16) :
#     print(apartment[i])
for _ in range(a) :
    floor = int(input())
    ho = int(input())
    print(apartment[floor+1][ho])
