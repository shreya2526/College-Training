def count_distinct_elements(arr, size):
    # Using a set to store unique elements
    distinct_elements = set()
    
    # Adding elements to the set
    for element in arr:
        distinct_elements.add(element)
    
    # Returning the count of distinct elements
    return len(distinct_elements)

# Example usage
arr = [1, 2, 2, 3, 4, 4, 5]
size = len(arr)
print("Number of distinct elements:", count_distinct_elements(arr, size))