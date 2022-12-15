/*

    파일위치 지시자에 대해서 조금 더 자세하게 얘기 할 계획이다.
    File Position Indicator
    지난번에 파일 위치 지시자에 관해서 대충 설명하고 나갔는데요,
    설명이 무언가 부족하다는 느낌이 강하게 들어서 다시 한번 짚고 넘어가도록 하겠습니다.
    스트림의 기본 모토는 바로 '순차적으로 입력을 받는다' 입니다.

    즉, 스트림에서 입력 받을 때에는 질서정연하게 앞에있는 데이터먼저 순서대로 읽어들이게 되죠.
    뒤에서부터 거꾸로 읽는다거나 데이터들을 뛰어넘으며 읽어 들인다는 듯한 비 정상적인 짓들을 
    하지 않습니다.
    이렇게 순차적으로 읽어들이는 것을 가능하게 해주는 것이 바로 파일 위치 지시자 입니다.


*/

#include <stdio.h>


int main(){

    FILE *fp;
    fp = fopen("some_data.txt","r");
    char c;
    if(fp == NULL){
        printf("file open error ! \n");
        return 0;
    }
    
    while((c = fgetc(fp)) != EOF){
        printf("%c",c);
    }



    return 0;
}


