#reverse the order of the words in a string

def revOrder(str1):
    words=str1.split()
    rev_list=words[::-1]
    s=' '.join(rev_list)
    return s

print(revOrder("Hello world"))