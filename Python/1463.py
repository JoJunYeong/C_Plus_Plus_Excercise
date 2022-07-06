import sys
input=sys.stdin.readline

target = int(input())

dynamicpro = [0]*(target+3)
dynamicpro[1],dynamicpro[2], dynamicpro[3] = 0,1,1

for i in range(3,target+1):
    minn=1e9
    if i%3==0 :
        minn=min(minn, dynamicpro[i//3])
    if i%2==0 :
        minn=min(minn, dynamicpro[i//2])
    minn=min(minn, dynamicpro[i-1])
    dynamicpro[i]= minn+1
# print(dynamicpro)
print(dynamicpro[target])



