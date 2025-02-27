package binarytrees;

/**
 * author: Thomas Okoyo
 * 
 * A BST is a binary tree with the ordering property: left child < parent < right child.
 * 
 * Use case: In-Memory Indexing in databases and quick lookup in search applications.
 */


class BSTNode {
    int value;
    BSTNode left;
    BSTNode right;

    public BSTNode(int value) {
        this.value = value;
    }
}

class BST {
    BSTNode root;

    public void insert(int value) {
        root = insertNode(root, value);
    }

    public BSTNode insertNode(BSTNode node, int value) {
        if (node == null) {
            return new BSTNode(value);
        }

        if (value < node.value) {
            node.left = insertNode(node.left, value);
        } else {
            node.right = insertNode(node.right, value);
        }

        return node;
    }

    public boolean search(int value) {
        return searchNode(root, value);
    }

    public boolean searchNode(BSTNode node, int value) {
        if (node == null) {
            return false;
        }

        if (node.value == value) {
            return true;
        }

        return value < node.value ? searchNode(node.left, value) : searchNode(node.right, value);
    }
}

public class BinarySearchTree {
    public static void main(String[] args) {
        BST bst = new BST();
        int [] values = {8, 3, 10, 1, 6, 14, 4, 7, 13};

        for (int value : values) {
            bst.insert(value);
        }

        System.out.println("BST Search results");
        System.out.println("Search 7: " + bst.search(7));
        System.out.println("Search 3: " + bst.search(3));
    }
}
