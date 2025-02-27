package binarytrees;

/**
 * author: Thomas Okoyo
 * 
 * AVL trees maintain a balance factor (difference between left and right subtree heights ≤ 1).
 * 
 * Balanced trees maintain a minimal height for efficiency. 
 * Two common types are AVL Trees and Red-Black Trees.
 * 
 * Use case: In-Memory Indexing in databases and quick lookup in search applications.
 */

class AVLNode {
    int key;
    int height;

    AVLNode left;
    AVLNode right;

    public AVLNode(int key) {
        this.key = key;
        this.height = 1;
    }
}

class AVLTree {
    private int height(AVLNode node) {
        return node == null? 0 : node.height;
    }

    private int getBalance(AVLNode node) {
        return node == null? 0 : height(node.left) - height(node.right);
    }

    private AVLNode rightRotate(AVLNode node) {
        AVLNode newParentNode = node.left;
        AVLNode holder = node.right;

        // perform rotation
        newParentNode.right = node; 
        node.left = holder;

        // update heights
        node.height = Math.max(height(node.left), height(node.right)) + 1;
        newParentNode.height = Math.max(height(newParentNode.left), height(newParentNode.right));

        return newParentNode;
    }

    private AVLNode leftRotate(AVLNode node) {
        AVLNode newParentNode = node.right;
        AVLNode holder = node.left;

        // perform rotations
        newParentNode.left = node;
        node.right = holder;

        // update heights
        newParentNode.height = Math.max(height(newParentNode.left), height(newParentNode.right)) + 1;
        node.height = Math.max(height(newParentNode.left), height(newParentNode.right)) + 1;

        return newParentNode;
    }

    public AVLNode insert(AVLNode node, int key) {
        if (node == null) {
            return new AVLNode(key);
        }

        if (key < node.key) {
            node.left = insert(node.left, key);
        } else {
            node.right = insert(node.right, key);
        }

        node.height = Math.max(height(node.left), height(node.right)) + 1;

        int balance = getBalance(node);

        // left left case
        if (balance > 1 && key < node.left.key) {
            return rightRotate(node);
        }

        // right right case
        if (balance < -1 && key > node.right.key) {
            return leftRotate(node);
        }

        // right left case
        if (balance < -1 && key < node.right.key) {
            node.right = rightRotate(node.right);
            return leftRotate(node);
        }

        return node;
    }

    public void preOrder(AVLNode node) {
        if (node != null) {
            System.out.println(node.key + " ");
            preOrder(node.left);
            preOrder(node.right);
        }
    }
}

public class AVLTreeExample {
    public static void main(String[] args) {
        AVLTree avlTree = new AVLTree();
        AVLNode root = null;

        int[] keys = {10, 20, 30, 40, 50, 25};

        for(int key: keys) {
            root = avlTree.insert(root, key);
        }

        System.out.println("AVL Tree Preorder Traversal");
        avlTree.preOrder(root);
    }
}
