W = sorted([int(input())for _ in range(10)])[7:]
K = sorted([int(input())for _ in range(10)])[7:]
print(sum(W), sum(K))

# w_lst=[]
# k_lst=[]
# for i in range(20) :
#     score = int(input())

#     if i<10 :   # W대학
#         if len(w_lst)==0 :
#             w_lst.append(score)
#         else :
#             for k in range(len(w_lst)) :
#                 if k==len(w_lst)-1 :
#                     w_lst.append(score)
#                 if w_lst[k] > score :
#                     continue
#                 elif w_lst[k] < score :
#                     w_lst.insert(k,score)
#                     break
                

# # 여기까지 짰고, 이제 K대학도 W대학처럼 하면 된다. 그 후에 앞에서 3개 더해주면 된다.
#     else :      # K대학
#         if len(k_lst)==0 :
#             k_lst.append(score)
#         else :
#             for k in range(len(k_lst)) :
#                 if k==len(k_lst)-1 :
#                     k_lst.append(score)
#                 if k_lst[k] > score :
#                     continue
#                 elif  k_lst[k] < score:
#                     k_lst.insert(k,score)
#                     break
# # print(f'w_lst={w_lst}')
# # print(f'k_lst={k_lst}')
# print(f'{w_lst[0]+w_lst[1]+w_lst[2]} {k_lst[0]+k_lst[1]+k_lst[2]}')