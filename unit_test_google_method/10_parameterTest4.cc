
#include <gtest/gtest.h>

class StringTest : public testing::TestWithParam<std::string> { };


//1. testing::Values
/*
    INSTANTIATE_TEST_SUITE_P(SampleValues, SampleTest,
        testing::Values(
            User(10,"Tom"),
            User(20,"Bob"),
            User(30,"Alice")
        ));
    이렇게 처리하지 말고 아예 데이터 셋을 불러 올 수 있다.
    testing::Values 가 아닌,  testing::ValuesIn을 사용하면 된다.
    배열뿐만 아니라, 컨테이너(벡터,디큐 등)도 사용 가능하다.
    물론 벡터같은 것을 리턴하는 함수도 넣을 수 있다.
*/

std::string names[]= {"Tom", "Alice", "Bob"};
INSTANTIATE_TEST_SUITE_P(SampleValues, SampleTest,
        testing::ValuesIn(names));

TEST_P(StringTest, Sample){
    std::cout<< GetParam() << std::endl;
}


