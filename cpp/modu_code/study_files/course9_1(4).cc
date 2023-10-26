// 타입이 아닌 템플릿 인자 (non-type template arguments)

// 한 가지 재미있는 점은 템플릿 인자로 타입만 받을 수 있는 것이 아닙니다. 예를 들어 아래와 같은 코드를 보실까요.
#include <iostream>
#include <array>

template <typename T, int num>
T add_num(T t) {
  return t + num;
}


template <typename T>
void print_array(const T& arr) {
  for (int i = 0; i < arr.size(); i++) {
    std::cout << arr[i] << " ";
  }
  std::cout << std::endl;
}


int main() {
  int x = 3;
  std::cout << "x : " << add_num<int, 5>(x) << std::endl;

  std::array<int, 5> arr = {1, 2, 3, 4, 5};
  std::array<int, 7> arr2 = {1, 2, 3, 4, 5, 6, 7};
  std::array<int, 3> arr3 = {1, 2, 3};

  print_array(arr);
  print_array(arr2);
  print_array(arr3);
}