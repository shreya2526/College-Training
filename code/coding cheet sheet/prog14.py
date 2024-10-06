#middle of a linkedlist

'''
node f=head;
node s=head;
while(f.next!=null){
    f=f.next.next;
    s=s.next;
}
return s.data;
'''