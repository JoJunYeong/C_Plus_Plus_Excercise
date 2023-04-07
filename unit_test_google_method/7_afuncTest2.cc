#include <string>
#include <iostream>

class Image{
    std::string url;

    public :
        Image(const std::string& s)
        :url(s)
        {

        }
        
        void Draw() const{
            std::cout << "Draw Image: " << url << std::endl;
        }

        /*
            객체에 대한 메모리 할당/해지의 동작을 재정희 해주어야 한다.
            new Image
            1) 메모리 할당 => operator new
            2) 생성자 호출 => operator new 자동동작

            * testcode에서 메모리 검증을 위해서는 아래 코드가 
                제품코드에 미리 정의되어져 있어야 한다.

            조건부 컴파일을 통해, 테스트 코드에서만 빌드되도록 제어하는 것이 좋다.
            g++ 7_afuncTest2.cc -lgtest-L -I ./googletest/googletest/include/ -pthread -DGTEST_LEAK_TEST

        */
        static int alloc;

        void* operator new(size_t size){
            ++alloc;
            return malloc(size);
        }


        /*
            delete p;
            1) 소멸자 호출
            2) 메모리 해지 => operator delete 자동동작
        
        */
        void operator delete(void* p, size_t){
            free(p);
            --alloc;
        }


};

int Image::alloc = 0;


void DrawImage(const std::string& url){
    Image* image = new Image(url);
    image->Draw();
    delete image;

}


// ----

#include <gtest/gtest.h>

// DrawImage를 수행할 때, Image 객체의 메모리 해지가
// 제대로 되는지 여부를 검증하고 싶다.
#ifdef DGTEST_LEAK_TEST
TEST(ImageTest, DrawImage){
    int alloc = Image::alloc;
    DrawImage("https://a.com/a.jpg");
    int diff = Image::alloc - alloc;
    EXPECT_EQ(diff,0) << diff << "object(s) leaked";

}
#endif

// 사용자 정의 테스트 스위트 클래스를 통해 
// 메모리 누수를 검증하고자 한다.
class ImageTest2 : public testing::Test{
    protected:
        int alloc= 0;
        void SetUp() override{
            alloc = Image::alloc;
        }
        void TearDown() override{
            int diff = Image::alloc -alloc;
            EXPECT_EQ(diff,0) << diff << "object(s) leaked";
        }



};

#ifndef DGTEST_LEAK_TEST
TEST_F(ImageTest2, DrawImage){
    DrawImage("https://a.com/a.jpg");
}
#endif

