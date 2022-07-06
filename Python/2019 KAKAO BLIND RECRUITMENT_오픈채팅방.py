from collections import defaultdict

def solution(record):
    answer = []

    lst=[]
    dic=defaultdict()
    for i in range(len(record)) :
        lst.append(record[i].split())

    for i in range(len(lst)) :
        # print(f'i={i} dic={dic}')
        if (lst[i][1] not in dic) and (lst[i][0] != 'Leave'):
            dic[lst[i][1]] = lst[i][2]
        if (lst[i][0] == 'Enter') and (lst[i][2]!= dic[lst[i][1]]) :
            # print(f'lst[{i}][2]={lst[i][2]} dic[lst[{i}][1]]={dic[lst[i][1]]}')
            dic[lst[i][1]] = lst[i][2]
        if lst[i][0] == 'Change' :
            dic[lst[i][1]] = lst[i][2]
    # print(lst)

    for i in range(len(lst)) :
        if lst[i][0] == 'Enter' :
            answer.append((dic[lst[i][1]]+'님이 들어왔습니다.'))
        elif lst[i][0] == 'Leave' :
            answer.append((dic[lst[i][1]]+'님이 나갔습니다.'))

    # print(answer)
    return answer


a= ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(a)

