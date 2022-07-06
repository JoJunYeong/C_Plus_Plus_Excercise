#list로 숫자 입력 받기
lst = list(map(int,list(input() for _ in range(10))))
sum=0
for i in range(1,10) :
    sum+=lst[i]
print(lst[0]-sum)
