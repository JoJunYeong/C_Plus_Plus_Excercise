#include <gtest/gtest.h>

// 6. 테스트 필터
// 원하는 테스트를 선택할 수 있는 기능을 제공
// $ ./a.out --gtest_filter=ImageTest.foo:ImageTest.goo:ImageTest.hoo

// 와일드 카드도 사용할 수 있다.
// $ ./a.out --gtest_filter=ImageTest.*
// $ ./a.out --gtest_filter=*.foo
// $ ./a.out --gtest_filter=Image*.*

// 제외도 가능하다.
// $ ./a.out --gtest_filter=ImageTest*.*:-*.goo

/*
    원하는 종류의 테스트를 선택적으로 수행할 수 있다.
    => 테스트 케이스를 만들 때, 이름 규칙을 잘 결정하는 것이 좋다.
    *테스트의 성격에 따라서 접두를 사용했다.
    P_Openfile, N_Openfile, X_Openfile
    => 가독성 뿐 아니라 필터의 기능을 활용하는데 도움이 된다.
*/



// ImageTest.foo
TEST(ImageTest, foo) { }

// ImageTest.goo
TEST(ImageTest, goo) { }

// ImageTest.hoo
TEST(ImageTest, hoo) { }

TEST(ImageProcessorTest, foo) { }
TEST(ImageProcessorTest, goo) { }
TEST(ImageProcessorTest, hoo) { }


/*
    7. 테스트 무작위 / 반복
        단위 테스트는 어떤 순서로 몇번을 구동해도
        동일한 결과가 수행되어야 한다. => "신뢰성"
        반복해서 무작위로 수행하는 방법
        ./a.out --gtest_repeat=10 --gtest_shuffle

        그러나 이런경우 실패지점을 찾아가야되는 경우가 있다.
        그래서 실패한다면 멈추는 옵션도 존재한다.
        --gtest_break_on_failure
        ./a.out --gtest_repeat=10 --gtest_shuffle --gtest_break_on_failure

        이렇게 하는 이유는 "변덕스러운 테스트"를 검출하기 위해서이다.

*/

int cnt = 0;
int GetCount() {return ++cnt;}

TEST(SampleTest7, Sample1){
    EXPECT_EQ(GetCount(),1);
}

TEST(SampleTest7, Sample2){
    EXPECT_EQ(GetCount(),2);
}






/*
    8. 테스트 결과 파일출력(formatter)
        => xUnit Test Framework
        테스트의 결과를 XML형식으로 export 한다.
        $ ./a.out --gtest_output=xml

        => Google Test 1.10 이후
        : json 형식으로 export 기능을 추가적으로 제공한다.
        $ ./a.out --gtest_output=json
    
*/

TEST(Sampletest8, Sample1){
    FAIL() << "실패!";
}






/*
    9. test_detail.xml / test_detail.json
    > 추가적인 정보도 기록할 수 있다.

*/

#define SPEC(message) do{ printf("SPEC: " message "\n"); RecordProperty("spec",message); }while(0)


TEST(SampleTest8, Sample1){
    SPEC("이미지 프로세서에서 이미지를 리사이즈를 검증한다.");
    RecordProperty("cpu", "1.5");
    RecordProperty("mem", "30%");

    FAIL() << "실패!";
}



