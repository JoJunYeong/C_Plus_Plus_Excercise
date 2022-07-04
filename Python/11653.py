num = int(input())


def nanugi(j) :
    for i in range(2,10000000) :
        if j % i == 0 :
            j = j / i
            print(i)
            break
    return j

while True :
    if(num>3) :
        num = nanugi(num)
    elif num == 1 :
        break
    else : 
        print(int(num))
        break










            
    