num = input()
num = int(num)
lst = list(input().split() for _ in range(int(num)))


for i in range(num) :
    print("Case #"+str(i+1)+": "+lst[i][0]+" + "+lst[i][1]+" = "+str(int(lst[i][0])+int(lst[i][1])))











