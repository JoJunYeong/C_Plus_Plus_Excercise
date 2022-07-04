def solution(s):
    answer = 0
    lenn = len(s)
    untill_lenn = lenn//2
    minn=lenn+1
    result=''
    if lenn==1 :
        minn=1
    else :
        for i in range(1,untill_lenn+1) :
            result_lenn=0
            result_string=''
            same_cnt=1
            for j in range(0,lenn,i) :
                
                if j ==0 :
                    tmp=s[0:i]
                else :
                    if s[j:j+i] == tmp :    # 이전 문자랑 다음문자가 같으면 
                        same_cnt+=1
                        # print('enter1')
                    else :    # 이전 문자랑 다음문자가 다르면
                        if same_cnt == 1 :
                            # print('enter2')
                            result_string += tmp
                            tmp=s[j:j+i]
                        else :
                            # print('enter3')
                            result_string += str(same_cnt)
                            result_string += tmp
                            tmp=s[j:j+i]
                            same_cnt=1
                    
                
                # print(f'i={i}, j={j}, same_cnt={same_cnt},tmp={tmp}, s[j:j+i]={s[j:j+i]}, result_string={result_string}')
            if same_cnt == 1 :
                # print('enter2')
                result_string += tmp
                tmp=s[j:j+i]
            else :
                # print('enter3')
                result_string += str(same_cnt)
                result_string += tmp
                tmp=s[j:j+i]
                same_cnt=1
            # print(f'i={i}, j={j}, same_cnt={same_cnt},tmp={tmp}, s[j:j+i]={s[j:j+i]}, result_string={result_string}')
            result_lenn = len(result_string)
            if minn > result_lenn :
                # print(f'minn={minn}, result_lenn={result_lenn}')
                minn = result_lenn
                result=result_string


    # print(f'minn={minn}, result={result}')
    




    return minn

a="aabbaccc"
b="ababcdcdababcdcd"
c="abcabcdede"
d="abcabcabcabcdededededede"
e="xababcdcdababcdcd"

solution(e)
