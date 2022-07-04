import time

hour , min2 = map(int, input().split() )
add = int(input())

print(str((hour+int((min2+add)/60))%24)+" "+str((min2+add)%60))



