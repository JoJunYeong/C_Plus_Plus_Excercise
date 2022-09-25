/*
문제 1
사용자로 부터 5 명의 학생의 수학, 국어, 영어 점수를 입력 받아서 
평균이 가장 높은 사람 부터 평균이 가장 낮은 사람까지 정렬되어 출력하도록 하세요. 
특히, 평균을 기준으로 평균 이상인 사람 옆에는 '합격', 
아닌 사람은 '불합격' 을 출력하게 해보세요 (난이도 : 中上).
*/

#include <stdio.h>

void MaxOrder(int *parr, int *student, int *Avg);
void Input(int *parr, int *student, int *Avg);
void PrintAns(int *parr, int *student, int *Avg);

int main(){
    int arr[5], student[5]={1,2,3,4,5};
    int avg=0;


    // printf("avg = %d\n",avg);
    Input(arr,student,&avg);
    MaxOrder(arr,student,&avg);
    PrintAns(arr,student,&avg);


    return 0;
}

void Input(int *parr, int *student, int *Avg) {

    for(int i =0 ; i <5 ;i++){
        int math=0, korean=0,english=0;
        printf("\n학생%d 수학 : ",i+1);
        scanf("%d", &math);
        printf("학생%d 국어 : ",i+1);
        scanf("%d", &korean);
        printf("학생%d 영어 : ",i+1);
        scanf("%d", &english);
        parr[i] = (int)((math+korean+english)/3);
        *Avg += parr[i];
    }
    *Avg = (int)(*Avg/5);
}

void MaxOrder(int *parr, int *student, int *Avg) {
    
    int pass = 0;
    
    while(!pass){
        for(int i = 0 ; i < 4 ; i++){
            if(parr[i] < parr[i+1])  {
                int tmp = parr[i];
                parr[i] = parr[i+1];
                parr[i+1] = tmp;
                tmp = student[i];
                student[i] = student[i+1];
                student[i+1] = tmp;
                break;
            }
            if(i==3)
                pass = !pass;
        }
    }
}

void PrintAns(int *parr,  int *student, int *Avg){
    
    for(int i=0;i<5;i++){
        printf("학생%d 평균: %d점 전체평균: %d점 결과:",student[i],parr[i], *Avg );
        if(parr[i]>=*Avg)
            printf(" 합격\n");
        else
            printf(" 불합격\n");
    }
}



