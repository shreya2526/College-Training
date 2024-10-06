def rearrange(arr):
    positive = [x for x in arr if x > 0]
    negative = [x for x in arr if x < 0]
    
    result = []
    j, k = 0, 0

    while j < len(positive) and k < len(negative):
        result.append(positive[j])
        result.append(negative[k])
        j += 1
        k += 1

    result.extend(positive[j:])
    result.extend(negative[k:])
    
    return result

arr = [-1, 3, 2, -9, 5, -4]
print(rearrange(arr))
