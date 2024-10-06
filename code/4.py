def fun(s, min,n):
    if n<min:
        print("invalid")
        return
    
    if s[0].isdigit():
        print("invalid")
        return

    cap,num,sep=0,0,0

    for i in range(0,n):
        if(s[i]==' ' or s[i]=='+'):
            print("invalid")
            return
        if(s[i]>='A' and s[i]<='Z'):
            cap+=1
        if(s[i].isdigit()):
            num+=1
        if(s[i]=='!' or s[i]=='@' or s[i]=='#' or s[i]=='$' or s[i]=='%' or s[i]=='^' or s[i]=='&' or s[i]=='*' or s[i]=='(' or s[i]==')' or s[i]=='-' or s[i]=='_' or s[i]=='=' or s[i]=='{' or s[i]=='}' or s[i]=='[' or s[i]==']' or s[i]==':' or s[i]==';' or s[i]==',' or s[i]=='/' or s[i]=='?' or s[i]=='.' or s[i]=='<' or s[i]=='>'):
            sep+=1
        
    if cap>0 and num>0 and sep>0:
        print("Valid")
    else:
        print("invalid")

s="aB1 7"
fun(s, 5, len(s))