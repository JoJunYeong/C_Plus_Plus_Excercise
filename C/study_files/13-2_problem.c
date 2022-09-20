// problem1 start
#include <stdio.h>

void PrintBigToSmall(int *parr);
void BubbleSort(int *parr);

int main(){
    int arr[10];
    for(int i = 0; i<10 ; i++)
        scanf("%d",&arr[i]);

    PrintBigToSmall(arr);

    return 0;
}


void PrintBigToSmall(int *parr){
    printf("\n");
    BubbleSort(parr);
    for(int i = 0 ; i < 10 ; i++){
        printf("%d ",parr[i]);
    }
    printf("\n");
}

void BubbleSort(int *parr){

    int done = 0;
    while(!done){
        
        for(int i = 0 ; i < 9 ; i++){
            if(parr[i] < parr[i+1]){
                int tmp = parr[i];
                parr[i] = parr[i+1];
                parr[i+1] = tmp;
                break;
            }
            if(i==8)
                done = 1;
        }

    }


}

// problem1 end




// problem2 start



// problem2 end





