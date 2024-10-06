def equivalent(s1, s2):
    string1=''.join(s1)
    string2=''.join(s2)

    return string1==string2

print(equivalent(["a","bc"], ["ab","c"]))