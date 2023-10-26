#include <iostream>


int& func(int& input_x){
    input_x +=1;
    return input_x;
}


int main(){

    int a = 1;
    int& b = func(a);
    int c = func(a);
    std::cout << "a= "<< a << "    b= " << b <<"    c= " << c << std::endl;
    a+=1;
    std::cout << "a= "<< a << "    b= " << b <<"    c= " << c << std::endl;


    return 0;
}