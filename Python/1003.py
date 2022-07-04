

tmp0_0=1    # 0의 0에서 등장횟수
tmp0_1=0    # 0의 1에서 등장횟수
tmp1_0=0    # 1의 0에서 등장횟수
tmp1_1=1    # 1의 1에서 등장횟수

iteration = int(input())

for i in range(iteration) :
    tmp0_0=1    # 0의 0에서 등장횟수
    tmp0_1=0    # 0의 1에서 등장횟수
    tmp1_0=0    # 1의 0에서 등장횟수
    tmp1_1=1    # 1의 1에서 등장횟수
    a=int(input())
    if a==0 :
        print(f'{tmp0_0} {tmp1_0}')
    elif a== 1 :
        print(f'{tmp0_1} {tmp1_1}')

    else :

        for j in range(a-1) :
            
            if j % 2 == 0 :
                tmp = tmp0_0 + tmp0_1
                tmp0_0 = tmp
                tmp = tmp1_0 + tmp1_1
                tmp1_0 = tmp
                if j == a-2 :
                    print(f'{tmp0_0} {tmp1_0}')
            else :
                tmp = tmp0_0 + tmp0_1
                tmp0_1 = tmp
                tmp = tmp1_0 + tmp1_1
                tmp1_1 = tmp
                if j == a-2 :
                    print(f'{tmp0_1} {tmp1_1}')
            # print(f'number={j+2}  tmp0_0={tmp0_0} tmp0_1={tmp0_1} tmp1_0={tmp1_0} tmp1_1={tmp1_1} ')
