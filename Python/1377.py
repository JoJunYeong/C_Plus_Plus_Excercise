import sys

input = sys.stdin.readline

number = int(input())
answer = []
number_lst=[]
for i in range(number) :
    number_lst.append((i,int(input())))

number_lst2 = sorted(number_lst, key=lambda x:x[1])
maxx = 0
for i in range(number) :
    maxx = max(maxx,number_lst2[i][0]-number_lst[i][0])

print(maxx+1)







