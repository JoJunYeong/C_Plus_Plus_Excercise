
import sys

input = sys.stdin.readline

matrix_row, matrix_column, end_time = map(int,input().split())
matrix = list(list(map(int, input().split())) for _ in range(matrix_row))
matrix_coordinate_move= list([0]*matrix_column for _ in range(matrix_row))


row_upperside_aircondition, row_downside_aircondition = 0, 0
column_rightside_matix = matrix_column-1
column_leftside_matix = 0
row_upperside_matrix = 0
row_downside_matrix = matrix_row-1

# 처음 2중 for문 돌면서 모든 초기값 세팅
for i in range(matrix_row) :
    for j in range(matrix_column) :
        # -1위치저장용 if문
        if matrix[i][j] == -1 and row_upperside_aircondition == 0  : 
            row_upperside_aircondition = i
            matrix_coordinate_move[i][j] = (i,j+1)
            row_downside_aircondition = i+1
            matrix_coordinate_move[i+1][j] = (i+1,j+1)

        # matrix_coordinate_move 데이터 삽입 구간
        # 맨위
        if i == 0 :
            if j == 0 :
                matrix_coordinate_move[i][j] = (i+1,j)
            else :
                matrix_coordinate_move[i][j] = (i,j-1)
        # 맨아래
        elif i == matrix_row-1 :
            if j == 0 :
                matrix_coordinate_move[i][j] = (i-1,j)
            else :
                matrix_coordinate_move[i][j] = (i,j-1)
        # 맨왼쪽
        elif j == 0 and (i!=0 or i!=matrix_row-1) :
            if row_upperside_aircondition == 0  :
                matrix_coordinate_move[i][j] = (i+1,j)
            elif i > row_downside_aircondition :
                matrix_coordinate_move[i][j] = (i-1,j)
        # 맨오른쪽
        elif j == matrix_column-1 and i!= 0 :
            if row_upperside_aircondition == 0 or row_upperside_aircondition == i :
                matrix_coordinate_move[i][j] = (i-1,j)
            elif i >= row_downside_aircondition :
                matrix_coordinate_move[i][j] = (i+1,j)
        # 공기청정기 위쪽 and 아래쪽
        elif (i == row_upperside_aircondition or i == row_downside_aircondition) and  (j != matrix_column-1 or j == 0):
                matrix_coordinate_move[i][j] = (i,j+1)
        # 나머지 안움직이는 애들
        else :
            matrix_coordinate_move[i][j] = (i,j)


def step1 (matrix):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    matrix_before_calculate=matrix
    matrix_after_calculate = list([0]*matrix_column for _ in range(matrix_row))
    matrix_after_calculate[row_upperside_aircondition][0] = -1
    matrix_after_calculate[row_downside_aircondition][0] = -1
    for i in range(matrix_row) :
        for j in range(matrix_column) :
            if matrix_before_calculate[i][j] != 0 and matrix_before_calculate[i][j] != -1 :
                cnt=0
                for k in range(4) :
                    x= j+dx[k]
                    y= i+dy[k]
                    if 0<=x<matrix_column and 0<=y<matrix_row and matrix_before_calculate[y][x] != -1 :
                        cnt+=1

                side_value = (matrix_before_calculate[i][j]//5)
                center_value = matrix_before_calculate[i][j] - side_value*cnt
                matrix_after_calculate[i][j] += center_value
                for k in range(4) :
                    x= j+dx[k]
                    y= i+dy[k]
                    if 0<=x<matrix_column and 0<=y<matrix_row and matrix_before_calculate[y][x] != -1:
                        matrix_after_calculate[y][x] += side_value
    # print(f'matrix_after_calculate={matrix_after_calculate}')
    return matrix_after_calculate          
    
def step2(matrix) :
    matrix_before_move = matrix
    matrix_after_move = list([0]*matrix_column for _ in range(matrix_row))
    global matrix_coordinate_move
    for i in range(matrix_row) :
        for j in range(matrix_column) :
            y,x=matrix_coordinate_move[i][j]
            if matrix_before_move[i][j] == -1 :
                matrix_after_move[y][x] = 0
            elif matrix_before_move[y][x] == -1 :
                matrix_after_move[y][x] = -1
            else :
                matrix_after_move[y][x]=matrix_before_move[i][j]
    # print(f'matrix_after_move={matrix_after_move}')
    return matrix_after_move

def process(matrix) :
    tmp_matrix=step1(matrix)
    return step2(tmp_matrix)  


def result(matrix) :
    summ=0
    for i in range(matrix_row) :
        summ += sum(matrix[i])
    return summ+2


for i in range(end_time) :
    matrix=process(matrix)
    # print(f'after_matrix={matrix}')


# print(f'end_matrix={matrix}')
print(result(matrix))
