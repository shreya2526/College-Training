class ll {
    node head;
    
    class node {
        int data;
        node next;
        
        node(int val) {
            data = val;
            next = null;
        }
    }
    
    public void insertion(int val) {
        node n = new node(val);
        if (head == null) {
            head = n;
        } else {
            node temp = head;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = n;
        }
    }
    
    public int middle() {
        node slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow.data;
    }
}

class find_middle_ll {
    public static void main(String[] args) {
        ll l = new ll();
        l.insertion(1);
        l.insertion(2);
        l.insertion(3);
        l.insertion(4);
        l.insertion(5);
        l.insertion(6);
        
        System.out.println(l.middle()); // Output: 3
    }
}
