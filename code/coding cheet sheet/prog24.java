class Node {
    int data;
    Node left, right;

    public Node(int item) {
        data = item;
        left = right = null;
    }
}

class prog24 {
    Node root;

    // Recursive function for inorder traversal
    void inorderTraversal(Node node) {
        if (node == null)
            return;

        // Traverse the left subtree
        inorderTraversal(node.left);

        // Visit the root node
        System.out.print(node.data + " ");

        // Traverse the right subtree
        inorderTraversal(node.right);
    }

    // Recursive function for preorder traversal
    void preorderTraversal(Node node) {
        if (node == null)
            return;

        // Visit the root node
        System.out.print(node.data + " ");

        // Traverse the left subtree
        preorderTraversal(node.left);

        // Traverse the right subtree
        preorderTraversal(node.right);
    }

    public static void main(String[] args) {
        prog24 tree = new prog24();
        tree.root = new Node(1);
        tree.root.left = new Node(2);
        tree.root.right = new Node(3);
        tree.root.left.left = new Node(4);
        tree.root.left.right = new Node(5);

        System.out.println("Inorder traversal of binary tree is:");
        tree.inorderTraversal(tree.root);

        System.out.println("\nPreorder traversal of binary tree is:");
        tree.preorderTraversal(tree.root);
    }
}
