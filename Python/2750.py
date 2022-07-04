# sort를 쓰는게 아니라, 버블정렬, 삽입정렬을 묻는 문제였음.


a= int(input())

lst=list(int(input()) for _ in range(a))

lst.sort()
for i in range(len(lst)) :
    print(lst[i])