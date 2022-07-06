


def solution(n, times):
    answer = 0
    times.sort
    a= times[0]
    lenn=len(times)
    max_time = a*n
    time_lst=[]
    time_lst2=[]
    # for i in range(len(times)) :
    #     # print(f'{i} enter, times[{i}]={times[i]}, max_time={max_time}')
    #     a = times[i]
    #     k=0
    #     while True :
    #         k+=a
    #         if (k)<= max_time :
    #             time_lst.append(k)

    #         else :
    #             break
    cnt=0
    for i in range(n-1) :
        k=0
        while True :
            print(f'k={k}, i={i}, len(times)={len(times)}')
            if k>=lenn :
                break
            if k==lenn-1 :
                if time_lst[k] < time_lst[0] :
                    time_lst[k] += times[k]
                    time_lst.append(time_lst[k])
                    print(f'k={k}, i={i}, cnt={cnt}, time_lst={time_lst}')
                    break
            elif time_lst[k] > time_lst[k+1] :
                k+=1
                continue
            else :
                time_lst[k] += times[k]
                time_lst.append(time_lst[k])
                print(f'k={k}, i={i}, cnt={cnt}, time_lst={time_lst}')
                break
    # time_lst.sort()
    print(time_lst)
    print(time_lst[n-1])

    return time_lst[n-1]




solution(6,[7,10])
solution(10,[6,8,10])
