def anagram(s,t):
    if len(s)==len(t):
        # Convert strings to lists, sort them, and then compare
        str1=sorted(s)
        str2=sorted(t)

        if str1==str2:
            return True
        else:
            return False
    return False

s="anagram"
t="nagaram"
print(anagram(s,t))