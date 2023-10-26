// 가변길이 템플릿

#include <iostream>

template <typename T>
void print(T arg) {
    std::cout << arg << std::endl;
}

template <typename T, typename... Types>    // typename 뒤에 ... 으로 오는 것을 템플릿 파리미터 팩(parameter pack) 이라고 부릅니다.
// 템플릿 파라미터 팩의 경우 0 개 이상의 템플릿 인자들을 나타냅니다.
void print(T arg, Types... args) {
    std::cout << arg << ", ";
    print(args...);
}

int main() {

    print(1,3.1,"abc");
    print(1,2,3,4,5,6,7);

}



