#include <stdio.h>


int main(){

    FILE *fp;
    char path[5000];

    scanf("Enter path that you want: %s", path);
    
    fp = fopen(path,"w");
    if(fp == NULL){
        printf("ERROR\n");
        return 0;
    }

    fputs('a',fp);
    fclose(fp);
    




    return 0;
}