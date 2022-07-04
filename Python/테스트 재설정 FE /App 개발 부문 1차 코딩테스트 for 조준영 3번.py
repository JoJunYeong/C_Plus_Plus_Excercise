def solution(width, height, diagonals):
    from itertools import combinations
    answer = 0
    total_cnt = 0
    map_coordinate = list([j,i] for i in range((2*width)+1) for j in range((2*height)+1))
    print(map_coordinate)
    for i in diagonals :
        map_original = list([0]*((2*width)+1) for _ in range((2*height)+1))
        number = 0
        for h in range((2*height)+1) :
            for w in range((2*width)+1) :
                map_original[h][w] = number
                if number == 0:
                    number=1
                elif number==1 :
                    number=0
        # 대각선 만들어주는 함수
        map_original[(2*(height-i[1]))+1][(2*i[0])-1] = 1
        

        # 이제 combination사용해서 각 높이와 너비간에 대각선 한번 건넜을때 최소거리를 구하고 그 값에 맞는 조합만 cnt시킨다.
        tmp_cnt=0
        for j in combinations(map_coordinate,(2*(width+height+1))+1) :
            tmpp=0
            for k in j  :
                y,x=k
                tmpp+=map_original[y][x]
            if tmpp==width+height+1 :
                tmp_cnt+=1
        





        total_cnt += tmp_cnt
    print(total_cnt)




    answer = total_cnt % 10000019
    return answer


n1,n11,n111 = 2,2,[[1,1],[2,2]]
n2,n22,n222 = 51,37,[[17,19]]

solution(n1,n11,n111)
# solution(n2,n22,n222)


