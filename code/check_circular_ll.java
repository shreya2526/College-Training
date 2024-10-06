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
    
    public boolean circular() {
        if (head == null) return false;

        node fast = head, slow = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            if (fast == slow) {
                return true;
            }
        }
        return false;
    }
    
    // Helper method to make the list circular by connecting last node to the middle node
    public void makeCircular() {
        if (head == null) return;
        
        // Find the middle node
        node slow = head, fast = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        
        // Find the last node
        node last = head;
        while (last.next != null) {
            last = last.next;
        }
        
        // Make the last node point to the middle node
        last.next = slow;
    }
}

class check_circular_ll {
    public static void main(String[] args) {
        ll l = new ll();
        l.insertion(1);
        l.insertion(2);
        l.insertion(3);
        l.insertion(4);
        l.insertion(5);
        l.insertion(6);

        // Make the list circular by connecting the last node to the middle node
        l.makeCircular();
        
        System.out.println(l.circular()); // Output: true
    }
}
