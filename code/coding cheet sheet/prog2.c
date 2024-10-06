#include <stdio.h>

void main()
{
    int k = 0;
    int arr[] = {0, 0, 0, 4, 3, 0, 5, 0};
    int n = 8;
    int temp;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] != 0)
        {
            temp = arr[k];
            arr[k] = arr[i];
            arr[i] = temp;
            k++;
        }
    }
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
}