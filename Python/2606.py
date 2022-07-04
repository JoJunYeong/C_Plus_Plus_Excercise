from collections import defaultdict

a= int(input())
b= int(input())
status = [True]*(a+1)
visit=[]
dic=defaultdict()
for i in range(b) :
    tmp1,tmp2=map(int,input().split())
    if tmp1 not in dic :
        dic[tmp1]=[tmp2]
    else :
        dic[tmp1]+=[tmp2]
    if tmp2 not in dic :
        dic[tmp2]=[tmp1]
    else :
        dic[tmp2]+=[tmp1]
# print(dic,'\n')
node=dic[1].pop()
visit.append(node)
status[1] = False
while node :
    # print(status)
    # print(f'node={node}')
    # print(dic,'\n')
    status[node] = False
    if node not in dic or len(dic[node]) == 0  :
        if len(visit)== 0 :
            break
        node=visit.pop()
    else :
        node=dic[node].pop()
        visit.append(node)
    

print(status.count(False)-1)




