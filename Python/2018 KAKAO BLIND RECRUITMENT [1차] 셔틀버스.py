def solution(n, t, m, timetable):
    answer = ''
    from  collections import deque

    min_time_table = deque()
    shuttle_time_interval=deque()
    for i in range(540,540+(n*t),t) :
        shuttle_time_interval.append([i,0])
    # print(f'shuttle_time_interval={shuttle_time_interval}')
    lst=[]
    for i in range(len(timetable)) :
        hour,min_t = map(int,timetable[i].split(":"))
        lst.append(hour*60+min_t)
    lst.sort()
    for i in range(len(lst)) :
        hour = lst[i]//60
        min_t = lst[i]-(hour*60)
        passs=False
        for j in range(len(shuttle_time_interval)) :
            if(60*hour)+min_t <= shuttle_time_interval[j][0] :
                # print(f'{hour}:{min_t}!!')
                # print(f'1shuttle_time_interval={shuttle_time_interval}')
                # print(f'lst={lst}')
                # print(f'lst={lst[i]}')
                shuttle_time_interval[j][1]+=1
                if shuttle_time_interval[j][1] >= m :
                    # print(f'2shuttle_time_interval={shuttle_time_interval}')
                    # print(f'{hour}:{min_t}!!')
                    tmp = (hour*60)+min_t-1
                    hour = tmp//60
                    min_t = tmp-(hour*60)
                    # passs=True
                    break

            if j==len(shuttle_time_interval)-1 :
                if shuttle_time_interval[j][1] - shuttle_time_interval[j-1][1] >m :
                    # print(f'3shuttle_time_interval[j][1] - shuttle_time_interval[j-1][1]={shuttle_time_interval[j][1] - shuttle_time_interval[j-1][1]}')
                    # print(f'shuttle_time_interval={shuttle_time_interval}')
                    # print(f'timetable[i]={timetable[i]}')
                    # print(f'{hour}:{min_t}!!')
                    tmp = (hour*60)+min_t-1
                    hour = tmp//60
                    min_t = tmp-(hour*60)
                    # passs=True
                    break
                else :
                    hour = shuttle_time_interval[j][0]//60
                    min_t = int(shuttle_time_interval[j][0])-int(hour*60)
        if passs :
            break
            # else :
            #     break
    # print(shuttle_time_interval)
    
    if hour < 10 :
        answer+='0'
        answer+=str(hour)
    else :
        answer+=str(hour)
    answer+=':'
    if min_t < 10 :
        answer+='0'
        answer+=str(min_t)
    else :
        answer+=str(min_t)

    print(f'answer={answer}')
    
    return answer



n1,t1,m1,timetable1 = 1,1,5,["08:00", "08:01", "08:02", "08:03"]
n2,t2,m2,timetable2 = 2,10,2,["09:10", "09:09", "08:00"]
n3,t3,m3,timetable3 = 2,1,2,["09:00", "09:00", "09:00", "09:00"]
n4,t4,m4,timetable4 = 1,1,1,["23:59"]
n5,t5,m5,timetable5 = 1,1,5,["00:01", "00:01", "00:01", "00:01", "00:01"]

# solution(n1,t1,m1,timetable1)
# solution(n2,t2,m2,timetable2)
# solution(n3,t3,m3,timetable3)
# solution(n4,t4,m4,timetable4)
# solution(n5,t5,m5,timetable5)