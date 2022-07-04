
# heapq 라이브러리 사용
import sys
import heapq

input=sys.stdin.readline

number=int(input())
lst=[]

for i in range(number) :
    numm = int(input())
    if numm == 0 :
        if len(lst) == 0 :
            print(0)
            continue
        else :
            print((heapq.heappop(lst))[1])
    else :
        heapq.heappush(lst,[-numm,numm])





# 라이브러리 사용하지 않음 => 삽입 구현까지 함
# import sys

# input=sys.stdin.readline

# number=int(input())
# lst=[]

# def heap_push_and_arrange_top_max_value(list,target) :
#     list.append(target)
#     target_index=len(list)-1
#     print(f'진입')
#     while True :
        
#         print(f'while진입')
        
#         print(f'list={list}, target_index={target_index}, target={target}')
#         if target_index%2==0 :
#             ttmp=target_index-2
#             if ttmp < 0 :
#                 ttmp=0
#             print(f'target={target}, target_index={target_index}, parents=list[{ttmp//2}]={list[ttmp//2]}')
#             print(f'진입 전')
#             if target > list[ttmp//2]  : # (list[target_index]-1)//2 ==> Parents index
#                 print(f'진입')
#                 parents_index=ttmp//2
#                 if parents_index < 0 :
#                     parents_index=0
#                 tmp=list[parents_index]
#                 list[parents_index]= list[target_index]
#                 list[target_index] = tmp
#             else :
#                 print(f'while탈출1')
#                 break
#         else :
            
#             ttmp=target_index-1
#             if ttmp < 0 :
#                 ttmp=0
#             print(f'target={target}, target_index={target_index}, parents=list[{ttmp//2}]={list[ttmp//2]}')
#             if target > list[ttmp//2]  : # (list[target_index]-2)//2 ==> Parents index
                
#                 parents_index=ttmp//2
#                 if parents_index < 0 :
#                     parents_index=0
#                 tmp=list[parents_index]
#                 list[parents_index]= list[target_index]
#                 list[target_index] = tmp
#             else :
#                 print(f'while탈출2')
#                 break
#         if parents_index == 0 : # 부모의 index가 0인 과정을 끝내면 break
#             print(f'while탈출3')
#             break
#         target_index=list.index(target)


# # def heap_max_pop(list) :









# for i in range(number) :
#     num=int(input())
#     if num==0 :
#         print(lst)
#     else :
#         heap_push_and_arrange_top_max_value(lst,num)




