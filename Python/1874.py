from collections import deque
import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)


a=int(input())
Fail=False
dq= deque()
result_lst=[]
stack_num=1
for i in range(a) :
    target = int(input())

    while True : # Target을 만날때까지 계속해서 돌아가는 반복문
        # print(f'stack_num={stack_num}, dq={dq}')
        # print(f'result_lst={result_lst}')
        if len(dq)==0 :
            dq.append(stack_num)
            result_lst.append('+')
            stack_num+=1
        else :
            if dq[-1] < target :
                dq.append(stack_num)
                result_lst.append('+')
                stack_num+=1
            elif dq[-1] > target :
                if len(dq)==0 :
                    print('NO')
                    Fail=True
                    break
                dq.pop()
                result_lst.append('-')
            elif dq[-1] == target :
                if len(dq)==0 :
                    print('NO')
                    Fail=True
                    break
                dq.pop()
                result_lst.append('-')
                break
            if stack_num>a+1 :
                print('NO')
                Fail=True
                break
    if Fail == True :
        break

if Fail == False :
    for i in range(len(result_lst)) :
        print(result_lst[i])



