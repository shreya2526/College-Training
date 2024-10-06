def checkAnagram(s,t):
    if( len(s) != len(t)):
        return False
    size=26
    arr=[0]*size

    for i in range(len(s)):
        arr[ord(s[i]) - ord('a')] += 1
        arr[ord(t[i]) - ord('a')] -= 1

    for i in range(len(s)):
        if arr[i]!=0:
            return False
    
    return True

print(checkAnagram("aman","nama"))