import sys

input = sys.stdin.readline

buffer=''
number_count = int(input())
matrix_original = list(list(map(int,input().rstrip())) for _ in range(number_count))

def bunhal_jungbok(magnitude, matrix) :
    check_matrix_1 = list([1]*magnitude for _ in range(magnitude))
    check_matrix_0 = list([0]*magnitude for _ in range(magnitude))
    global buffer
    if matrix == check_matrix_1 :
        buffer+='1'
    elif matrix == check_matrix_0 :
        buffer+='0'   
    else :
        new_magnitude=magnitude//2
        buffer+='('
        bunhal_jungbok(new_magnitude,[send_matrix[0:new_magnitude] for send_matrix in matrix[0:new_magnitude]])
        bunhal_jungbok(new_magnitude,[send_matrix[new_magnitude:new_magnitude*2] for send_matrix in matrix[0:new_magnitude]])
        bunhal_jungbok(new_magnitude,[send_matrix[0:new_magnitude] for send_matrix in matrix[new_magnitude:new_magnitude*2]])
        bunhal_jungbok(new_magnitude,[send_matrix[new_magnitude:new_magnitude*2] for send_matrix in matrix[new_magnitude:new_magnitude*2]])
        buffer+=')'


bunhal_jungbok(number_count,matrix_original)


print(buffer)



