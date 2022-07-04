# 섹시한 다른사람 풀이

import sys
n=int(sys.stdin.readline())
 
color_paper=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]#x행 y열
 
white=0#0이면 흰생
blue=0#1이면 파란색
 
def cut(x,y,n):
    global blue,white
    check=color_paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check!=color_paper[i][j]:#하나라도 같은색이 아니라면
                #4등분
                cut(x,y,n//2)#1사분면
                cut(x,y+n//2,n//2)#2사분면
                cut(x+n//2,y,n//2)#3사분면
                cut(x+n//2,y+n//2,n//2)#4사분면
                return
 
 
    if check==0:#모두 흰색일때
        white+=1
        return
    else:   #모두 파란색일때
        blue+=1
        return
 
 
cut(0,0,n)
print(white)
print(blue)



# 밑에는 내 풀이

# a=int(input())

# matrix_original = list(list(map(int,input().split())) for _ in range(a))
# matrix_white = list([False] * a for _ in range(a))
# matrix_blue = list([False] * a for _ in range(a))
# white_cnt=0
# blue_cnt=0
# check_size = a

# for i in range(a) :
#     for j in range(a) :
#         if matrix_original[i][j]==0 :
#             matrix_white[i][j] = True
#         else :
#             matrix_blue[i][j] = True

# while True :
#     x,y=0,0
#     while True :
#         # print(f'check_size={check_size}, x={x}, y={y}')
#         if x>= a  :
#             y+=check_size
#             x=0
#         if y>= a  :
#             break
#         white_tmp_cnt, blue_tmp_cnt = 0,0

#         for i in range(y,y+check_size) :
#             for j in range(x,x+check_size) :
#                 if matrix_white[i][j] == False :
#                     white_tmp_cnt+=1
#                 if matrix_blue[i][j] == False :
#                     blue_tmp_cnt+=1
#         # print(f'white_tmp_cnt={white_tmp_cnt}, blue_tmp_cnt={blue_tmp_cnt}')

#         if white_tmp_cnt == 0 :
#             white_cnt+=1
#             for i in range(y,y+check_size) :
#                 for j in range(x,x+check_size) :
#                     matrix_white[i][j] = False  
#         if blue_tmp_cnt == 0: 
#             blue_cnt+=1
#             for i in range(y,y+check_size) :
#                 for j in range(x,x+check_size) :
#                     matrix_blue[i][j] = False 


#         x+=check_size
#     if check_size==1 :
#         break
#     check_size//=2

# print(white_cnt)
# print(blue_cnt)




