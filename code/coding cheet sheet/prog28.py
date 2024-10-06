def countOccurrence(arr):
    ans = {}
    for elem in arr:
        if elem in ans:
            ans[elem] += 1
        else:
            ans[elem] = 1

    return ans

arr = [10, 5, 10, 15, 10, 5]
ans = countOccurrence(arr)

for key, value in ans.items():
    print(key, ':', value)
