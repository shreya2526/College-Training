def merge(num1, m, num2, n):
    # Start from the end of both num1 and num2
    i = m - 1
    j = n - 1
    k = m + n - 1

    # Merge in reverse order
    while i >= 0 and j >= 0:
        if num1[i] > num2[j]:
            num1[k] = num1[i]
            i -= 1
        else:
            num1[k] = num2[j]
            j -= 1
        k -= 1

    # If there are remaining elements in num2, copy them
    while j >= 0:
        num1[k] = num2[j]
        j -= 1
        k -= 1

# Example usage
num1 = [1, 2, 3, 0, 0, 0]
m = 3
num2 = [2, 5, 6]
n = 3

merge(num1, m, num2, n)
print(num1)  # Output: [1, 2, 2, 3, 5, 6]
