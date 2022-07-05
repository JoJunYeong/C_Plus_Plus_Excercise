



def solution(money, costs):
    answer = 0
    #money는 맞춰야되는 금액
    #costs는 각 가격별 생산단가
    cost_can_use = [True]*6
    remain_money = money
    total_cost = 0
    cost_1,cost_5,cost_10,cost_50,cost_100,cost_500 = costs[0],costs[1],costs[2],costs[3],costs[4],costs[5]
    ccost=[1,5,10,50,100,500]
    tmp = [0]*6
    tmp[5] = cost_500
    tmp[4] = cost_100*5
    tmp[3] = cost_50*10
    tmp[2] = cost_10*50
    tmp[1] = cost_5*100  
    tmp[0] = cost_1*500
    # print(f'tmp={tmp}')
    for i in range(5,-1,-1) :
        # print(f'entery remain_money={remain_money}, total_cost={total_cost}')
        if i!=0 :
            if remain_money//ccost[i] != 0:
                # print(f'passs ccost[i]={ccost[i]}')
                passs=False
                for j in range(i-1,-1,-1) :
                    # print('쨘')
                    if tmp[i] > tmp[j] :
                        passs=True
                        # print(f'걸러짐 tmp[i] > tmp[j]={tmp[i]} > {tmp[j]}    passs ccost[i]={ccost[i]}')
                        break
                if passs==False :
                    total_cost += (remain_money//ccost[i])*costs[i]
                    remain_money -= (remain_money//ccost[i])*ccost[i]
                else :
                    # print(f'calculate remain_money={remain_money}, total_cost={total_cost}, costs[i]={costs[i]}')
                    continue
                    
                
        else :
            # print('쨘')
            total_cost += (remain_money//ccost[i])*costs[i]
            remain_money -= (remain_money//ccost[i])*ccost[i]
            
            # print(f'calculate remain_money={remain_money}, total_cost={total_cost}, costs[i]={costs[i]}')

    # print(total_cost)
    return total_cost


a1,a2=4578,[1, 4, 99, 35, 50, 1000]
b1,b2=1999,[2, 11, 20, 100, 200, 600]

solution(a1,a2)
# solution(b1,b2)
