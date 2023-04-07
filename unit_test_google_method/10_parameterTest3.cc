
#include <gtest/gtest.h>


// 튜플타입
#if 0
class SampleTest:public testing::TestWithParam<std::tuple<int, std::string>> {

};

INSTANTIATE_TEST_SUITE_P(SampleValues, SampleTest,
    testing::Values(
        std::make_tuple(10,"Tom"),
        std::make_tuple(20,"Bob"),
        std::make_tuple(30,"Alice"),
    ));

TEST_P(SampleTest, Sample1){
    auto& param = GetParam();
    std::cout << std::get<0>(param) <<"," <<std::get<1>(param) << std::endl;
    FAIL();
}
#endif





//사용자 정의타입
class User{
    std::string name;
    int age;
    public :
        User(int n, const std::string& s)
        :name(s),age(n){

        }
        // 사용자 정의 타입을 출력하는 연산자 오버로딩 함수를 제공해야 한다.
        friend std::ostream& operator<<(std::ostream&os, const User&user){
            return os << user.name << ", " << user.age;
        }
};   


class SampleTest:public testing::TestWithParam<User> {

};

INSTANTIATE_TEST_SUITE_P(SampleValues, SampleTest,
    testing::Values(
        User(10,"Tom"),
        User(20,"Bob"),
        User(30,"Alice")
    ));

TEST_P(SampleTest, Sample1){
    const User& param = GetParam();
    FAIL();
}

