h,m,s = map(int, input().split())
plus = input()
plus = int(plus)
time = (h*3600)+(m*60)+s+plus
h = int((time/3600)%24)
time = time%3600
m = int(time/60)
time = time%60
print(h,m,time)



