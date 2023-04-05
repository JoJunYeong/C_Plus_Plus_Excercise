// 1_start.cc
#include <gtest/gtest.h>


// how to add testcase
TEST(sample,Test1) {

}


// Google Test main 함수형태는 일정함.
// > libgtest.a 안에 main함수를 포함시켜서 테스트 코드를 작성할 때 main을 
// 생략할 수 있다.
#if 0
int main(int argc, char** argv)
{
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
#endif
// how to build code.
// $ g++ 1_start.cc -lgtest -L. -I./googletest/googletest/include/ -pthread



