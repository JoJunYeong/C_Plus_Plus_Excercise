



def solution(relation):
    from itertools import combinations

    answer = 0
    len_relation = len(relation)
    len_relation2=len(relation[0])
    # 0-학번 1-아름 2-전공 3-학년 
    independent_check = [True]*len_relation2
    check_num=[]
    for i in range(len_relation2) :
        tmp_lst=[]
        for j in range(len_relation) :
            if relation[j][i] in tmp_lst :
                independent_check[i] = False  # 각 세로줄의 독립성 조사
                check_num.append(i)
                break
            tmp_lst.append(relation[j][i])
    check_num=[i for i in range(len_relation2)] 
    # 각 세로줄 독립성 조사 완료

    # print(independent_check)
    # print(check_num)
    check=[]
    for k in range(1,len(check_num)+1) :
        
        for i in combinations(check_num,k) :
            # 여기에서 이녀석을 구성하고 있는 녀석의 전 단계가 독립성을 인정받은적이 있는지 검사.
            # print(f'check={check}')
            continuee=False
            if len(check)!=0 :
                # print('enter')
                for x in range(len(check)) :
                    passs=0
                    tmp_string=''
                    tmp_string2=''
                    for y in range(len(i)) :
                        tmp_string2+=str(i[y])
                    for yy in range(len(check[x])) :
                        if tmp_string2.find(str(check[x][yy])) != -1 :
                            passs+=1
                        # print(f'check={check}, tmp_string={tmp_string} , check[{x}][{y}]={check[x][y]}')
                    # print(f'i={i} i[x]={i[x]}, len(i)={len(i)}')
                    
                    # print(f'{tmp_string}.find({tmp_string2})={tmp_string.find(tmp_string2)}')
                    # if tmp_string.find(tmp_string2)!=-1 or tmp_string2.find(tmp_string)!=-1 :
                    #     passs=1
                    # print(f'passs={passs}')
                    if passs == len(check[x]) :
                        continuee=True
                        # print('continue')
                        break
            if continuee :
                continue                

            independent_check_tmp = True
            # print(i)
            tmp_lst=[]
            for w in range(len(relation)) :
                tmp_string=''
                for q in i :
                    tmp_string+=str(relation[w][q])
                    # print(f'q={q}, tmp_string={tmp_string}')
                if tmp_string in tmp_lst :
                    independent_check_tmp = False
                    break
                
                tmp_lst.append(tmp_string)
                # print(f'tmp_lst={tmp_lst}, independent_check_tmp={independent_check_tmp}')
            # print(f'tmp_lst={tmp_lst}, independent_check_tmp={independent_check_tmp}')
            if independent_check_tmp :
                # print(f'len({i})={len(i)}')
                answer=len(i)
                check.append(list(i))
                # 여기에서 통과된 녀석의 구성원을 저장하는것이 좋아보인다. 그래야 위의 검사에 사용될 수 있다.
                # print(f'append check={check}')




    # print(check)
    print(len(check))
    return len(check)



a=[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
b=[["100","100","ryan","music","2"], ["200","200","apeach","math","2"], ["300","300","tube","computer","3"], ["400","400","con","computer","4"], ["500","500","muzi","music","3"], ["600","600","apeach","music","2"]]
c=[['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']]
d=[["a","1","aaa","c","ng"],
["a","1","bbb","e","g"],
["c","1","aaa","d","ng"],
["d","2","bbb","d","ng"]]
solution(a)