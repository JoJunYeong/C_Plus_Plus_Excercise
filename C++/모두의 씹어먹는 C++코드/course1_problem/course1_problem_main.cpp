#include "course1_problem.h"

int main(){
    course1_problem course1;
    
    course1.SetDate(2022,07,02);
    course1.ShowDate();
    course1.AddDay(30);
    course1.ShowDate();
    course1.AddMonth(10);
    course1.ShowDate();
    course1.AddYear(1000);
    course1.ShowDate();

    return 0;
}