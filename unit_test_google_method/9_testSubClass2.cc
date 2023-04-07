#include <iostream>

class Engine{
    public:
        virtual ~Engine() { }

        virtual void Start(){   // 가상함수이기때문에 테스트 전용 하위 클래스 패턴을 통해 해결할 수 있다.
            std::cout << "Engine Start" << std::endl;
        }
};

class Car{
    Engine* engine;

    public:
        Car(Engine* p)
        : engine(p)
        {

        }

        void Go(){

            // 내부조건이 적절이 수행되면 아래를 수행한다.
            engine->Start();
        }
};


#include <gtest/gtest.h>

/*
    검증하고자 하는 내용
    Car의 Go가 호출되었을 때, Engine의 Start가 제대로 호출되었는지 여부를
    검증하고 싶다.

    > 문제점 : Engine의 Start가 호출되었는지 여부를 확인할 수 있는 기능이 SUT에 제공되지 않는다.
                테스트 코드에서 단언문을 제공할 수 없다.

    핵심 : 가상함수 =>테스트 전용 하위 클래스 패턴을 통해 문제를 해결할 수 있다.
    Test class에서 Engine이 갖고 있는 Start를 override한다면, 
    그럼 가상함수이기때문에 Test의 경우에는 test의 Start가 실행 될 것이다.

*/

class TestEngine : public Engine {
    bool isStart = false;

    public:
        void Start() override {
            Engine::Start();    // 부모의 기능을 그대로 호출한다.
            // 테스트 검증을 위한 상태를 변경한다.
            isStart = true;
        }

        bool IsStart() const {return isStart;}
};



TEST(CarTest, Engine){

    TestEngine engine;
    Car car(&engine);

    car.Go();

    EXPECT_TRUE(engine.IsStart()) << "Car가 Go 성공하였을 때";
}



