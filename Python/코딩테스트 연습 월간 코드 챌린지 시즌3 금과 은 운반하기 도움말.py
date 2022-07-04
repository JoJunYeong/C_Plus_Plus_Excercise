


def solution(a, b, g, s, w, t):

    answer = -1
    many=len(g)
    status = [True]*many
    time=0
    remain =0
    exit=0
    while exit==0 :
        time+=1
        for i in range(many) :
            if time%t[i] ==0 and status[i] == True :  # 운반가능시간이고, 운반가능상태일때
                if a>=b : # 금을 우선적으로 소진시킨다 남은거 중에 금이 더 많은 경우고, 그러면서 도시에 금이 있는경우
                    if a >=w[i] :   # 운반가능한 양보다 필요로 남은 금의 양이 많다면
                        if g[i] >= w[i] :   # 도시에 남은 금이 운반가능양보다 많다면 그냥진행
                            a-=w[i]
                            g[i]-=w[i]  # 도시에 남은 금 총량도 빼준다
                        elif g[i] < w[i] and g[i]>0: # 만약에 도시에 남은 금이 운반가능양보다 적다면  
                            tmp=w[i]    # 남은 금을 트럭에 싣고 남는만큼 은을 옮기려고 시도한다
                            tmp-=g[i]   
                            g[i]=0
                        elif g[i] < w[i] and g[i]==0 : # 애초에 금이 0이면
                            if s[i] >= tmp :   # 도시에 남은 은이 남은운반가능양보다 많다면 그냥진행
                                b-=tmp
                                s[i]-=tmp  # 도시에 남은 은 총량도 빼준다
                            elif s[i] < w[i] and s[i]>0: # 만약에 도시에 남은 은이 운반가능양보다 적다면  
                                b-=s[i]    # 남은 은을 트럭에 싣는다.  
                                s[i]=0
                            if s[i] >= tmp :   # 도시에 남은 은이 남은운반가능양보다 많다면 그냥진행
                                b-=tmp
                                s[i]-=tmp  # 도시에 남은 은 총량도 빼준다
                            elif s[i] < w[i] and s[i]>0: # 만약에 도시에 남은 은이 운반가능양보다 적다면  
                                b-=s[i]    # 남은 은을 트럭에 싣는다.  
                                s[i]=0
                        if a<=0 and b<=0 :  # 만약에 도착지의 필요량이 금/은 모두 0이하면 종료한다.
                            print(time)
                            exit=1  # while문 탈출코드
                            break   # for문 탈출코드
                    else :   # 운반가능한 양이 필요로 남은 금의 양보다 크다면 
                        tmp=w[i]    # 필요한만큼 남은 금을 트럭에 싣고 남는만큼 은을 옮기려고 시도한다
                        tmp-=a
                        a=0
                        if s[i] >= tmp :   # 도시에 남은 은이 남은운반가능양보다 많다면 그냥진행
                            b-=tmp
                            s[i]-=tmp  # 도시에 남은 은 총량도 빼준다
                        elif s[i] < w[i] and s[i]>0 : # 만약에 도시에 남은 은이 운반가능양보다 적다면  
                            b-=s[i]    # 남은 은을 트럭에 싣는다.  
                            s[i]=0
                        elif s[i] < w[i] and s[i]==0 : # 애초에 은이 0이면
                            if g[i] >= tmp :   # 도시에 남은 금이 남은운반가능양보다 많다면 그냥진행
                                a-=tmp
                                g[i]-=tmp  # 도시에 남은 금 총량도 빼준다
                            elif g[i] < w[i] and g[i]>0: # 만약에 도시에 남은 금이 운반가능양보다 적다면  
                                a-=g[i]    # 남은 금을 트럭에 싣는다.  
                                g[i]=0
                            elif g[i] < w[i] and g[i]==0 : # 애초에 금이 0이면
                                if s[i] >= tmp :   # 도시에 남은 은이 남은운반가능양보다 많다면 그냥진행
                                    b-=tmp
                                    s[i]-=tmp  # 도시에 남은 은 총량도 빼준다
                                elif s[i] < w[i] and s[i]>0: # 만약에 도시에 남은 은이 운반가능양보다 적다면  
                                    b-=s[i]    # 남은 은을 트럭에 싣는다.  
                                    s[i]=0
                        if a<=0 and b<=0 :
                            print(time)
                            exit=1  # while문 탈출코드
                            break   # for문 탈출코드
                elif a<b : # 이번엔 남은거중에 은이 더 많은경우
                    if b >=w[i] :   # 운반가능한 양보다 필요로 남은 은의 양이 많다면
                        if s[i] >= w[i] :   # 도시에 남은 은이 운반가능양보다 많다면 그냥진행
                            b-=w[i]
                            s[i]-=w[i]  # 도시에 남은 은 총량도 빼준다 
                        elif s[i] < w[i] and s[i]>0: # 만약에 도시에 남은 은이 운반가능양보다 적다면  
                            tmp=w[i]    # 남은 은을 트럭에 싣고 남는만큼 금을 옮기려고 시도한다
                            tmp-=s[i]   
                            s[i]=0
                            if g[i] >= tmp :   # 도시에 남은 금이 남은운반가능양보다 많다면 그냥진행
                                a-=tmp
                                g[i]-=tmp  # 도시에 남은 금 총량도 빼준다
                            elif g[i] < w[i] and g[i]>0: # 만약에 도시에 남은 금이 운반가능양보다 적다면  
                                a-=g[i]    # 남은 금을 트럭에 싣는다.  
                                g[i]=0
                        elif s[i] < w[i] and s[i]==0 : # 애초에 은이 0이면
                            tmp=w[i]    # 남은 은을 트럭에 싣고 남는만큼 금을 옮기려고 시도한다
                            tmp-=s[i]  
                            if g[i] >= tmp :   # 도시에 남은 금이 남은운반가능양보다 많다면 그냥진행
                                a-=tmp
                                g[i]-=tmp  # 도시에 남은 금 총량도 빼준다
                            elif g[i] < w[i] and g[i]>0: # 만약에 도시에 남은 금이 운반가능양보다 적다면  
                                a-=g[i]    # 남은 금을 트럭에 싣는다.  
                                g[i]=0
                        if a<=0 and b<=0 :  # 만약에 도착지의 필요량이 금/은 모두 0이하면 종료한다.
                            print(time)
                            exit=1  # while문 탈출코드
                            break   # for문 탈출코드
                    elif b <w[i] : # 운반가능한 양이 필요로 남은 은의 양보다 크다면 
                        if s[i] > 0 :
                            tmp=w[i]    # 필요한만큼 남은 은을 트럭에 싣고 남는만큼 금을 옮기려고 시도한다
                            tmp-=b
                            print(f'여기를 만남 b={b}, w[{i}]={w[i]}')
                            b=0
                            if g[i] >= tmp :   # 도시에 남은 금이 남은운반가능양보다 많다면 그냥진행
                                a-=tmp
                                g[i]-=tmp  # 도시에 남은 금 총량도 빼준다
                            elif g[i] < w[i] and s[i]>0 : # 만약에 도시에 남은 금이 운반가능양보다 적다면  
                                a-=g[i]    # 남은 금을 트럭에 싣는다.  
                                g[i]=0
                            elif g[i] < w[i] and g[i]==0 : # 애초에 금이 0이면
                                
                                if s[i] >= tmp :   # 도시에 남은 은이 남은운반가능양보다 많다면 그냥진행
                                    b-=tmp
                                    s[i]-=tmp  # 도시에 남은 은 총량도 빼준다
                                elif s[i] < w[i] and s[i]>0: # 만약에 도시에 남은 은이 운반가능양보다 적다면  
                                    b-=s[i]    # 남은 은을 트럭에 싣는다.  
                                    s[i]=0
                        if a<=0 and b<=0 :
                            print(time)
                            exit=1  # while문 탈출코드
                            break   # for문 탈출코드

                status[i] = False   # 작업을 수행하고 해당 도시의 트럭상태를 회수해야 되는 애로 바꾼다.
            elif time%t[i]==0 and status[i] == False : # 만약에 도시트럭의 상태가 회수를 기다리는 False라면
                status[i]=True  # 상태를 True로 바꿔주어서 운반이 간으한 상태임으로 만든다.

        # print(f'time={time}, a={a}, b={b}, g={g}, s={s}, w={w} status={status}')
    return time


solution(10,10,[100],[100],[7],[10])
solution(90,500,[70,70,0],[0,0,500],[100,100,2],[4,8,1])
