
from re import A


how_many = int(input())

score = list(int(input()) for _ in range(how_many))
dynamic = []
if how_many>0 :
    dynamic.append( score[0])
if how_many>1 :    
    dynamic.append( max(score[0]+score[1],score[1] ))
if how_many>2:
    dynamic.append( max(score[0]+score[2], score[1]+score[2]))

for i in range(3,how_many) :
    dynamic.append( max(dynamic[i-3]+score[i-1]+score[i], dynamic[i-2]+score[i]))

# print(dynamic)
print(dynamic.pop())





