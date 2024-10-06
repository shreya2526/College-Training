#include<stdio.h>

void main(){
    int i=0, j=0;
    int arr[] = {5, 7, 1, 7, 6, 0};
    int n = 6;

    for(i = 0; i < n; i++){
        int next = -1;  // Initialize the next greater element as -1
        for(j = i + 1; j < n; j++){
            if(arr[j] > arr[i]){
                next = arr[j];
                break;
            }
        }
        printf("%d ", next);
    }
}
