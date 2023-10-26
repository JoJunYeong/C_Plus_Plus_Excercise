class Vector{
public:
    explicit Vector(int size) {}    // explicit 을 사용하면 암시적 변환의 용도로 사용할 수 없다.
    // explicit을 사용하는 것 자체가 직접초기화만 가능하고, 복사초기화도 사용할 수 없다.
};

void foo(Vector v) {}   // Vector v = 3

int main(){

    Vector v1(3);
    Vector v2 = 3;
    Vector v3{3};
    Vector v4 = {3};

    v1 = 3; // explicit 때문에 error가 나게된다.
    
    foo(3);

}