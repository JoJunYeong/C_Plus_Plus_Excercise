# 본 문제에서 제시한 테트로미오는 3*3과 4*4를 빈칸없이 다 커버할 수 있다.
# 고로 연결된 4개의 정사각형 아무거나 더했을 때 최댓값이 나오는 것으로 구하면 된다.
# 좌표를 이용해보자 연결된 애들은 x좌표나 y좌표의 값 차이가 옆에녀석과 1밖에 안난다.

import sys
input=sys.stdin.readline

# 직선
def 직선(y,x,matrix,a,b) :
    if 0<=y<a and 0<=x<b-3 :
        직선1=matrix[y][x]+matrix[y][x+1]+matrix[y][x+2]+matrix[y][x+3]
    else :
        직선1=0
    if 0<=y<a-3 and 0<=x<b :    
        직선2=matrix[y][x]+matrix[y+1][x]+matrix[y+2][x]+matrix[y+3][x]
    else :
        직선2=0
    return max(직선1,직선2)

# 정사각
def 정사각(y,x,matrix,a,b) :
    if 0<=y<a-1 and 0<=x<b-1 :
        정사각1=matrix[y][x]+matrix[y][x+1]+matrix[y+1][x]+matrix[y+1][x+1]
    else :
        정사각1=0
    return 정사각1

# ㄴ자
def ㄴ자(y,x,matrix,a,b) :
    if 0<=y<a-2 and 0<=x<b-1 :
        ㄴ자1=matrix[y][x]+matrix[y+1][x]+matrix[y+2][x]+matrix[y+2][x+1]
    else :
        ㄴ자1=0
    if 0<=y<a-2 and 1<=x<b :
        ㄴ자2=matrix[y][x]+matrix[y+1][x]+matrix[y+2][x]+matrix[y+2][x-1]
    else :
        ㄴ자2=0
    if 0<=y<a-1 and 0<=x<b-2 :
        ㄴ자3=matrix[y][x]+matrix[y][x+1]+matrix[y][x+2]+matrix[y+1][x+2]
    else :
        ㄴ자3=0
    if 1<=y<a and 0<=x<b-2 :
        ㄴ자4=matrix[y][x]+matrix[y][x+1]+matrix[y][x+2]+matrix[y-1][x+2]
    else :
        ㄴ자4=0
    if 2<=y<a and 0<=x<b-1 :
        ㄴ자5=matrix[y][x]+matrix[y-1][x]+matrix[y-2][x]+matrix[y-2][x+1]
    else :
        ㄴ자5=0
    if 2<=y<a and 1<=x<b :
        ㄴ자6=matrix[y][x]+matrix[y-1][x]+matrix[y-2][x]+matrix[y-2][x-1]
    else :
        ㄴ자6=0
    if 0<=y<a-1 and 2<=x<b :
        ㄴ자7=matrix[y][x]+matrix[y][x-1]+matrix[y][x-2]+matrix[y+1][x-2]
    else :
        ㄴ자7=0
    if 1<=y<a and 2<=x<b :
        ㄴ자8=matrix[y][x]+matrix[y][x-1]+matrix[y][x-2]+matrix[y-1][x-2]
    else :
        ㄴ자8=0
    return max(ㄴ자1,ㄴ자2,ㄴ자3,ㄴ자4,ㄴ자5,ㄴ자6,ㄴ자7,ㄴ자8)
   
# 지그재그
def 지그재그(y,x,matrix,a,b) :
    if 0<=y<a-2 and 0<=x<b-1 :
        지그재그1=matrix[y][x]+matrix[y+1][x]+matrix[y+1][x+1]+matrix[y+2][x+1]
    else :
        지그재그1=0
    if 0<=y<a-2 and 1<=x<b :
        지그재그2=matrix[y][x]+matrix[y+1][x]+matrix[y+1][x-1]+matrix[y+2][x-1]
    else :
        지그재그2=0
    if 0<=y<a-1 and 0<=x<b-2 :
        지그재그3=matrix[y][x]+matrix[y][x+1]+matrix[y+1][x+1]+matrix[y+1][x+2]
    else :
        지그재그3=0
    if 1<=y<a and 0<=x<b-2 :
        지그재그4=matrix[y][x]+matrix[y][x+1]+matrix[y-1][x+1]+matrix[y-1][x+2]
    else :
        지그재그4=0
    if 2<=y<a and 0<=x<b-1 :
        지그재그5=matrix[y][x]+matrix[y-1][x]+matrix[y-1][x+1]+matrix[y-2][x+1]
    else :
        지그재그5=0
    if 2<=y<a and 1<=x<b :
        지그재그6=matrix[y][x]+matrix[y-1][x]+matrix[y-1][x-1]+matrix[y-2][x-1]
    else :
        지그재그6=0
    if 0<=y<a-1 and 2<=x<b :
        지그재그7=matrix[y][x]+matrix[y][x-1]+matrix[y+1][x-1]+matrix[y+1][x-2]
    else :
        지그재그7=0
    if 1<=y<a and 2<=x<b :
        지그재그8=matrix[y][x]+matrix[y][x-1]+matrix[y-1][x-1]+matrix[y-1][x-2]
    else :
        지그재그8=0
    return max(지그재그1,지그재그2,지그재그3,지그재그4,지그재그5,지그재그6,지그재그7,지그재그8)
# 빠큐
def 빠큐(y,x,matrix,a,b) :
    if 0<=y<a-1 and 1<=x<b-1 :
        빠큐1=matrix[y][x]+matrix[y+1][x]+matrix[y+1][x+1]+matrix[y+1][x-1]
    else :
        빠큐1=0
    if 1<=y<a-1 and 0<=x<b-1 :
        빠큐2=matrix[y][x]+matrix[y][x+1]+matrix[y+1][x+1]+matrix[y-1][x+1]
    else :
        빠큐2=0
    if 1<=y<a and 1<=x<b-1 :
        빠큐3=matrix[y][x]+matrix[y-1][x]+matrix[y-1][x+1]+matrix[y-1][x-1]
    else :
        빠큐3=0
    if 1<=y<a-1 and 1<=x<b :
        빠큐4=matrix[y][x]+matrix[y][x-1]+matrix[y+1][x-1]+matrix[y-1][x-1]
    else :
        빠큐4=0
    return max(빠큐1,빠큐2,빠큐3,빠큐4)


a,b = map(int,input().split())
matrix = list(list(map(int,input().split())) for _ in range(a))

maxx=0
# print(matrix)
for i in range(a) :
    for j in range(b) :
        maxx=max(maxx,직선(i,j,matrix,a,b),정사각(i,j,matrix,a,b),ㄴ자(i,j,matrix,a,b),지그재그(i,j,matrix,a,b),빠큐(i,j,matrix,a,b))

print(maxx)

