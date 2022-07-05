

def solution(n, clockwise):
    answer = [[]]

    # 결과를 기록/출력할 맵
    map_original = list([0]*n for _ in range(n))
    
    # 이동방향 0-북, 1-동, 2-남, 3-서
    dx=[0,1,0,-1]   
    dy=[-1,0,1,0]

    # 스타팅 포인트는 무조건 4개
    start_point=[]
    start_point.append([0,0])
    start_point.append([0,n-1])
    start_point.append([n-1,0])
    start_point.append([n-1,n-1])
    start1,start2,start3,start4=[0,0],[0,n-1],[n-1,0],[n-1,n-1] # [y,x] 왼쪽위, 오른쪽위, 왼쪽아래, 오른쪽아래
    map_original[0][0],map_original[0][n-1],map_original[n-1][0],map_original[n-1][n-1] = 1,1,1,1
    # 스타팅 포인트별 진행방향
    # clockwise == True면 0(북) -> 1 -> 2 -> 3
    # clockwise == False면 0(북) -> 3 -> 2 -> 1
    if clockwise    :
        start_dir = [1,2,0,3]
    else :
        start_dir = [2,3,1,0]
    # 각 포인트별 진행해도되는지 안되는지 판단 
    start_go=[True]*4

    number_stamp = 1
    while True :
        number_stamp+=1
        # 범위를 벗어나는 일은 없다. 고로 가려는 길에 숫자가 바뀌었는지만 판단하면 된다. 바뀌었으면 방향틀기, 틀었는데도 바뀌어있으면 해당포인트 진행 종료
        for i in range(4) :
            if start_go[i] == True :
                y,x=start_point[i]
                y+=dy[start_dir[i]]
                x+=dx[start_dir[i]]
                start_point[i][0],start_point[i][1] = y,x
                # print(f'number_stamp = {number_stamp} [{y},{x}], i={i}, start_point[i]={start_point[i]}, start_dir[i]={start_dir[i]}')
                map_original[y][x] = number_stamp
                tmp_x,tmp_y = x+dx[start_dir[i]], y+dy[start_dir[i]]
                if map_original[tmp_y][tmp_x] != 0 :
                    if clockwise :
                        start_dir[i] +=1
                        if start_dir[i] == 4 :
                            start_dir[i]=0
                        tmp_x,tmp_y = x+dx[start_dir[i]], y+dy[start_dir[i]]
                        if 0<=tmp_x<n and 0<=tmp_y<n :
                            if map_original[tmp_y][tmp_x] != 0 :
                                start_go[i] = False
                    else :
                        start_dir[i] -=1
                        if start_dir[i] == -1 :
                            start_dir[i]=3
                        tmp_x,tmp_y = x+dx[start_dir[i]], y+dy[start_dir[i]]
                        if 0<=tmp_x<n and 0<=tmp_y<n :
                            if map_original[tmp_y][tmp_x] != 0 :
                                start_go[i] = False
        cnt_0 = 0
        for i in range(n) :
            cnt_0 += map_original[i].count(0)

        if start_go.count(False) == 4 or cnt_0==0:
            break

    # print(map_original)

    return map_original







n1,n11 = 5,True
n2,n22 = 6,False
n3,n33 = 9,False


# solution(n1,n11)
# solution(n2,n22)
solution(n3,n33)


