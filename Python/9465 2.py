import sys

aa= int(input())

for _ in range(aa) :
    summ=0
    a = int(input()) 
    dp=[]
    dp.append([])
    dp.append([])
    lst=list(list(map(int,sys.stdin.readline().split())) for _ in range(2))
    for i in range(a) :
        if i==0 :
            dp[0].append(lst[0][i])
            dp[1].append(lst[1][i])
        elif i==1 :
            dp[0].append(lst[0][i]+dp[1][i-1])
            dp[1].append(lst[1][i]+dp[0][i-1])
        else :
            if dp[1][i-2]>dp[1][i-1] :
                dp[0].append(lst[0][i]+dp[1][i-2])
            else :
                dp[0].append(lst[0][i]+dp[1][i-1])
            
            if dp[0][i-2]>dp[0][i-1] :
                dp[1].append(lst[1][i]+dp[0][i-2])
            else :
                dp[1].append(lst[1][i]+dp[0][i-1])

    print(max(dp[0][a-1], dp[1][a-1]))


