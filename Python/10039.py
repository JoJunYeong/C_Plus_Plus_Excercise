lst = list(map(int, list(input() for _ in range(5))))


sum=0
for i in range(5) :
    if lst[i] < 40 :
        lst[i] = 40
    sum = sum+lst[i]

print(int(sum/5))


