def palindrome(s):
    char_list=list(s)
    for i in range(int((len(char_list))/2)):
        if char_list[i]!=char_list[-(i+1)]:
            return False
    return True

print(palindrome("madam"))