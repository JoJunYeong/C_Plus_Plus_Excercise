/*

문제 2
수학 관련 소프트웨어를 만드는 회사에서 의뢰가 들어왔습니다. 
중학생용 기하학 소프트웨어를 만드는 것인데요, 
클래스는 총 두 개로 하나는 Point 로 점에 관한 정보를 담는 것이고 다른 하나는 Geometry 로 점들을 가지고 연산을 하는 클래스 입니다. 
즉 아래와 같은 두 클래스의 함수들을 모두 정의하세요 (난이도 : 上)


*/

#include <iostream>

class Point {
  int x, y;

 public:
  Point(int pos_x, int pos_y);
  int GetX() const ;
  int GetY() const ;

};

<<<<<<< HEAD:C++/모두의 씹어먹는 C++코드/problem_files/course4_2/course2_problem2.cpp
=======
Point::Point(int pos_x, int pos_y){
    mX=pos_x;
    mY=pos_y;
 }

 int Point::XPointReturn(){
    return mX;
 }

 int Point::YPointReturn(){
    return mY;
 }
>>>>>>> e0ff43a926c894d8d99fe4676cebd7ed0f11dc37:C++/모두의 씹어먹는 C++코드/course2_problem/course2_problem2.cpp

class Geometry {
 public:
  Geometry() {
    num_points = 0;
  }

  void AddPoint(const Point &point) {
<<<<<<< HEAD:C++/모두의 씹어먹는 C++코드/problem_files/course4_2/course2_problem2.cpp
    point_array[num_points ++] = new Point(point.GetX() , point.GetY());
=======
    point_array[num_points ++] = new Point(point.mX, point.mY);
>>>>>>> e0ff43a926c894d8d99fe4676cebd7ed0f11dc37:C++/모두의 씹어먹는 C++코드/course2_problem/course2_problem2.cpp
  }

  // 모든 점들 간의 거리를 출력하는 함수 입니다.
  void PrintDistance();

  // 모든 점들을 잇는 직선들 간의 교점의 수를 출력해주는 함수 입니다.
  // 참고적으로 임의의 두 점을 잇는 직선의 방정식을 f(x,y) = ax+by+c = 0
  // 이라고 할 때 임의의 다른 두 점 (x1, y1) 과 (x2, y2) 가 f(x,y)=0 을 기준으로
  // 서로 다른 부분에 있을 조건은 f(x1, y1) * f(x2, y2) <= 0 이면 됩니다.
  void PrintNumMeets();

private:
  // 점 100 개를 보관하는 배열.
  Point* point_array[100];
  int num_points;

void PrintDistance(){

  for ( int i = 0 ; i < num_points ; i++) {
    for ( int j = i+1 ; j < num_points ; j++) {

      Point* point1 = point_array[i];
      Point* point2 = point_array[j];

      int p1X = point1->GetX(), p1Y = point1->GetY();
      int p2X = point2->GetX(), p2Y = point2->GetY();
      int distance = ((p1X-p2X)^2 - (p1Y-p2Y)^2)^(1/2);

      std::cout << distance << std::endl;

    }
  }
 

}

void PrintNumMeets(){

  for ( int i = 0 ; i < num_points ; i++) {
    for ( int j = i+1 ; j < num_points ; j++) {

      Point* point1 = point_array[i];
      Point* point2 = point_array[j];

      int p1X = point1->GetX(), p1Y = point1->GetY();
      int p2X = point2->GetX(), p2Y = point2->GetY();
      int distance = ((p1X-p2X)^2 - (p1Y-p2Y)^2)^(1/2);

      std::cout << distance << std::endl;

    }
  }

}



};

  



Point::Point(int pos_x, int pos_y){
  this->x = pos_x;
  this->y = pos_y;
}

int Point::GetX() const {
  return x;
}

int Point::GetY() const {
  return y;
}



