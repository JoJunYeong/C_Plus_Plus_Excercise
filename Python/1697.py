import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000000)

start, target = map(int,input().split())
cnt = 0
stop = 0

def start_func(number,cnt) :
    calculator_plus(number,cnt)
    calculator_minus(number,cnt)
    calculator_multiply(number,cnt)

def calculator_plus(number,cnt) :
    global target,stop
    number+=1
    cnt+=1
    print(f'cnt={cnt}, number={number},plus')
    if number == target :
        print(int(cnt))
        stop= -1
    elif stop ==  -1 :
        return 
    else :
        calculator_plus(number,cnt)
        calculator_minus(number,cnt)
        calculator_multiply(number,cnt)

def calculator_minus(number,cnt) :
    global target,stop
    number-=1
    cnt+=1
    print(f'cnt={cnt}, number={number},minus')
    if number == target :
        print(int(cnt))
        stop= -1
    elif stop ==  -1 :
        return 
    else :
        calculator_plus(number,cnt)
        calculator_minus(number,cnt)
        calculator_multiply(number,cnt)

def calculator_multiply(number,cnt) :
    global target,stop
    number*=2
    cnt+=1
    print(f'cnt={cnt}, number={number},multiply')
    if number == target :
        print(int(cnt))
        stop= -1
    elif stop ==  -1 :
        return 
    else :
        calculator_plus(number,cnt)
        calculator_minus(number,cnt)
        calculator_multiply(number,cnt)


start_func(start,0)

