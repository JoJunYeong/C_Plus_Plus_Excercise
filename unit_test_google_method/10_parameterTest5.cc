


#include <gtest/gtest.h>

enum Color{
    RED,   
    WHITE,
    BLACK
};

std::vector<std::string> cars = {
    "sonata", "avante", "genesis"
};

using CarType = std::tuple<std::string, int>;
clas CarTest : public testing::TestWithParam<CarType> {};

/*
    testing::combine
    => 두개 이상의 데이터르 ㄹ조합해서 사용할 수 있다.

*/


INSTANTIATE_TEST_SUITE_P(CarValues, CarTest,
        testing::Combone(
            testing::ValuesIn(cars),
            testing::Values(RED,WHITE,BLACK)));

TEST_P(CarTest,Sample){
    auto& param = GetParam();
    std::cout << std::get<0>(param) << ", " << std::get<1>(param) <<std::endl;
}
