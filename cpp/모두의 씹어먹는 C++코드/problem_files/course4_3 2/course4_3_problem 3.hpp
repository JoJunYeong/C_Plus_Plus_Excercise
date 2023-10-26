#include <iostream>
#include <string.h>

class string{
    char *mStr;
    int mLen;

    public:
        string(char c, int n);  // 문자 C가 N개 있는 문자열로 검색
        string(const char *s);
        string(const string &s);
        ~string();

        void add_string(const string &s);   // str뒤에 s를 붙인다.
        void copy_string(const string &s);  // str뒤에 s를 복사한다.
        int strlen () const;   // 문자열 길이 리턴

};