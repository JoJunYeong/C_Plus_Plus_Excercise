a=int(input())
judge=input()
cnt,cnt2=0,0
for i in range(a) :
    if judge[i:i+1] == 'A' :
        cnt+=1
    else :
        cnt2+=1
if cnt>cnt2 :
    print('A')
elif cnt<cnt2:
    print('B')
else :
    print('Tie')