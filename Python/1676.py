a=int(input())
facto=1
for i in range(1,a+1) :
    facto*=i
facto = str(facto)
facto=facto[::-1]
# print(facto)
for i in range(len(facto)) :
    if facto[i] !='0' :
        print(i)
        break



