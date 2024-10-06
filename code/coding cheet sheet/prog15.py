#linkedlist has a cycle or not

'''
node f=head.next;
node s=head;
while(f.next!=null && f!=s){
    f=f.next.next;
    s=s.next;
}
if(f!=s)
    return false;
return true;
'''