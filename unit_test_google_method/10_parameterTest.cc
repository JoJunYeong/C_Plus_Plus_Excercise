

bool IsPrime(int value){
    for(int i = 2 ; i< value ; i++){
        if (value % i == 0){
            return false;
        }
    }
    return true;
}

#include <gtest/gtest.h>

/*
    하나의 테스트 케이스 안에 여러개의 단언문을 작성하는 경우
    => EXPECT_
    아래와 같은 경우에서 단언문의 중복입력과 for문의 사용으로 인해 발생할 수 있는 
    유지보수 측면에서의 문제를 xUnit에서 해결할 수 있게 제공해준다.
*/

TEST(Primetest, IsPrime1){
    ASSERT_TRUE(IsPrime(2));
    ASSERT_TRUE(IsPrime(3));
    ASSERT_TRUE(IsPrime(5));
    ASSERT_TRUE(IsPrime(7));
}

TEST(Primetest, IsPrime2){
    ASSERT_TRUE(IsPrime(2));
    ASSERT_TRUE(IsPrime(3));
    ASSERT_TRUE(IsPrime(5));
    ASSERT_TRUE(IsPrime(7));
}

// 아니 왜 위처럼 번거롭게 하나? 쉽게 반복문 같은걸로 안되나?

TEST(Primetest, IsPrime3){
    int pv[] = {1,3,5,7,9,11,13,15};

    for(auto e : primeValues){
        EXPECT_TRUE(IsPrime(e));
    }
}


