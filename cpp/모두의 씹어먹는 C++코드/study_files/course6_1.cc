/*

6단원에서는 
C++ 표준 문자열 (std::string)
상속 (inheritance)
오버라이딩(overriding)
protected 키워드에 대해서 배웁니다.

이번 단원 6-1에서는 그중 string 문자열 클래스에 대해서 공부해보도록 하겠다.
*/


#include <iostream>
#include <string>

int main(){
    // 표준이기 때문에 std 안에 string이 정의되어 있다.
    // std = standard
    // STL = Standard Template Library (표준 템플릿 라이브러리)

    std::string s = "abc";
    std::string t = "def";
    std::string s2 = s;

    std::cout << s << " 의 길이 : " << s.length() << std::endl;
    std::cout << s << " 뒤에 " << t << "를 붙이면 : " << s + t << std::endl;

    if(s==s2){
        std::cout << s << " 와 " << s2 <<" 는 같다 " << std::endl;
    }
    if(s!=t){
        std::cout << s << " 와 " << t << " 는 다르다 " << std::endl;
    }


    return 0;
}






