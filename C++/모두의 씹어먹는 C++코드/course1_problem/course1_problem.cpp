#include "course1_problem.h"

// 생성자이다.
course1_problem::course1_problem(){
    std::cout << "Course1_problem class has been created" << std::endl;
    
}

course1_problem::~course1_problem(){
    std::cout << "Course1_problem class has been deleted" << std::endl;
}

// Date 함수 내부를 초기화 시키는 함수이다.
void course1_problem::SetDate(int year, int month, int date){
    year_ = year;
    month_ = month;
    day_ = date;
}

// x일을 원하는 만큼 더하게 된다.
void course1_problem::AddDay(int inc){
    day_ += inc;
    if(month_ == 1 || month_ == 3 || month_ == 5 || month_ == 7 || month_ == 8 || month_ == 10 || month_ == 12){
        if(day_ > 31){
            if(month_ == 12){
                month_=1;
                year_+=1;
            }
            else{
                month_+=1;
                day_-=31;
            }
        }
    }
    else if(month_ == 4 || month_ == 6 || month_ == 9 || month_ == 11){
        if(day_ > 30){
            month_+=1;
            day_-=30;
        }
    }
    else if(month_ == 2){
        if(day_>28){
            month_+=1;
            day_-=28;
        }
    }
}


// x달을 원하는 만큼 더하게 된다.
void course1_problem::AddMonth(int inc){
    month_ += inc;
    if(month_ > 12){
       month_ -=12;
       year_+=1;
    }
    
}

// x년을 원하는 만큼 더하게 된다.
void course1_problem::AddYear(int inc){
    year_ += inc;
}

// 현재 날짜 상태를 보여준다.
void course1_problem::ShowDate(){
    std::cout << year_ << "-" << month_ << "-" << day_ << std::endl;
}