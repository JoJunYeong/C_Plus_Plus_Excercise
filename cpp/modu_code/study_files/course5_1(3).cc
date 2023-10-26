/*

friend 키워드

*/

class A{
    private:
        void private_func(){}
        int private_num;

        // B는 A의 친구
        friend class B;

        // func 은 A의 친구
        friend void func(); 

};

class B{
    public:
        void b(){
            A a;

            // 비록 private 함수의 필드들이지만 친구이기 떄문에 접근 가능하다.
            a.private_func();
            a.private_num = 2;
        }
};

void func(){
    A a;
    
    // 비록 private 함수의 필드들이지만 위와 마찬가지로 친구이기 떄문에 접근 가능하다.
    a.private_func();
    a.private_num = 2;


}

int main(){
    
    return 0;
}













