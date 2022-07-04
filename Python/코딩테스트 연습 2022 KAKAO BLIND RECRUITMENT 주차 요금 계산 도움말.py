

def solution(fees, records):
    from collections import defaultdict
    import math
    answer = []
    calcuated_min_dic = defaultdict()
    calcuating_min_dic = defaultdict()
    for i in records :
        time, car_num, status = i.split()
        hour,minute = map(int,time.split(":"))
        total_time = (hour*60)+minute
        if status == 'IN' :
            calcuating_min_dic[car_num] = total_time
        else :
            if car_num not in calcuated_min_dic :
                calcuated_min_dic[car_num] = total_time - calcuating_min_dic[car_num]
                del(calcuating_min_dic[car_num])
            else :
                calcuated_min_dic[car_num] += total_time - calcuating_min_dic[car_num]
                del(calcuating_min_dic[car_num])
    reamin_lst =  sorted(calcuating_min_dic.items(), key = lambda x:x[0])  
    for i in reamin_lst :
        car_num, time = i[0], i[1]
        time = 1439 - time
        if car_num not in calcuated_min_dic :
            calcuated_min_dic[car_num] = time 
        else :
            calcuated_min_dic[car_num] += time 

    calculate_result_lst = sorted(calcuated_min_dic.items(), key = lambda x:x[0])
    for i in calculate_result_lst :
        if i[1] <= fees[0] :
            answer.append(fees[1])
        else :
            answer.append(fees[1]+(math.ceil((i[1] - fees[0]) / fees[2]) * fees[3]))
  
    return answer

# n1은 기본시간(분), 기본요금(원), 단위시간(분), 단위요금(원)
n1,n11 = [180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
n2,n22 = [120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
n3,n33 = [1, 461, 1, 10],["00:00 1234 IN"]

# solution(n1,n11)
solution(n2,n22)
# solution(n3,n33)




