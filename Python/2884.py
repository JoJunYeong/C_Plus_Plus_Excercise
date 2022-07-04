a,b=map(int,input().split())

time = a*60 + b - 45
print(int((time/60)%24),time%60)

