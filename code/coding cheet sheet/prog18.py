#palindrom

def CheckPalindrom(str1):
    s=str1.lower()
    for i in range(len(s)//2):
        if(s[i]!=s[-(i+1)]):
            return False
    return True

print(CheckPalindrom("Nadam"))