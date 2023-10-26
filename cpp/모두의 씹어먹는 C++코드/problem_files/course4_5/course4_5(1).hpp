#include <iostream>
#include <stdio.h>

class String{

private :

    char *mStr;
    int mStrLen;

public :
    String(char c); // string을 char로부터 생성
    String(char *c);    // string을 char *로부터 생성
    ~String();

    int StringLenth(String s);  // 문자열 길이를 구하는 함수
    void AddString(String s);   // 문자열 뒤에 다른 문자열 붙이기
    bool IsStringInside(String s);  // 문자열 내에 포함되어 있는 문자열 구하기
    bool IsSame(String s);  // 문자열이 같은지 비교
    bool IsFrontOfDictinary(String s); // 문자열 크기 비교 

};


