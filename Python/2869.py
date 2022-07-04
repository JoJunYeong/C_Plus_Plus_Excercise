a,b,c= map(int, input().split())
if int(((c-a)//(a-b))) != ((c-a)/(a-b)) :
    print(((c-a)//(a-b))+2)
elif int(((c-a)//(a-b))) == ((c-a)/(a-b)) :
    print(((c-a)//(a-b))+1)