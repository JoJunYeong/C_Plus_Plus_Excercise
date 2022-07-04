#자동차 비교개수
num = int(input())

for _ in range(num) :
    cost = int(input())
    option_num = int(input())
    lst = list(list(map(int,input().split())) for _ in range(option_num))
    for i in range(option_num) :
        cost += (lst[i][0]*lst[i][1])
    print(cost)