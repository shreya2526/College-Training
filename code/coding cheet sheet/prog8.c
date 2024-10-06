#include <stdio.h>

int isMagicalNumber(int num) {
    int sum = 0;
    
    // Convert to binary and modify digits
    while (num > 0) {
        int digit = num % 2;
        if (digit == 0)
            digit = 1;  // Replace 0 with 1
        else if (digit == 1)
            digit = 2;  // Replace 1 with 2
        
        sum += digit;
        num /= 2;
    }
    
    // Check if the sum is odd
    return sum % 2 != 0;
}

int countMagicalNumbers(int N) {
    int count = 0;
    
    for (int i = 1; i <= N; i++) {
        if (isMagicalNumber(i)) {
            count++;
        }
    }
    
    return count;
}

int main() {
    int N;
    printf("Enter N: ");
    scanf("%d", &N);
    
    int result = countMagicalNumbers(N);
    printf("Count of magical numbers from 1 to %d is: %d\n", N, result);
    
    return 0;
}
