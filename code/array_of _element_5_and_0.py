def largest_number_divisible_by_90(arr):
    count_5 = arr.count(5)
    count_0 = arr.count(0)
    
    # If there are no 0s, it's impossible to form a number divisible by 10
    if count_0 == 0:
        return 0
    
    # Determine the maximum number of 5s that make the sum divisible by 9
    # The sum of digits should be divisible by 9
    num_5s_to_use = (count_5 // 9) * 9
    
    # If no 5s can be used to satisfy divisibility by 9, return 0
    if num_5s_to_use == 0:
        return 0
    
    # Form the largest number
    largest_number = '5' * num_5s_to_use + '0' * count_0
    
    return largest_number

# Example usage
arr1 = [5, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5]
arr2 = [5, 0]

print(largest_number_divisible_by_90(arr1))  # Output: 5555555550
print(largest_number_divisible_by_90(arr2))  # Output: 0
