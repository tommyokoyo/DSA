package binarytrees;

/**
 * author: Thomas Okoyo
 * 
 * A binary tree restricts each node to two children (left and right).
 * 
 * Use case: Expression Trees used in compilers to parse and evaluate mathematical expressions.
 */

class BinaryTreeNode {
    int value;
    BinaryTreeNode left;
    BinaryTreeNode right;

    public BinaryTreeNode(int value) {
        this.value = value;
    }
}

public class BinaryTreeExample {
    // inorder traversal (left, root, right)
    public static void inOrderTraversal(BinaryTreeNode node) {
        if (node != null) {
            inOrderTraversal(node.left);
            System.out.println(node.value + " ");
            inOrderTraversal(node.right);
        }
    }

    public static void main(String[] args) {
        BinaryTreeNode root = new BinaryTreeNode(10);
        root.left = new BinaryTreeNode(5);
        root.right = new BinaryTreeNode(15);
        root.left.left = new BinaryTreeNode(3);
        root.left.right = new BinaryTreeNode(7);

        System.out.println("Binary Tree Node traversal:");
        inOrderTraversal(root);
    }
}
