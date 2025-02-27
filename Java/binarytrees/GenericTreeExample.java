package binarytrees;

import java.util.ArrayList;
import java.util.List;

/**
 * author: Thomas Okoyo
 * 
 * A generic tree lets each node have an arbitrary number of children (e.g., file systems).
 * 
 * Use case: File Systems and Organizational Charts where nodes have many children.
 */

class TreeNode {
    String value;
    List<TreeNode> children;

    public TreeNode(String value){
        this.value = value;
        this.children = new ArrayList<>();
    }

    public void addChild(TreeNode child){
        children.add(child);
    }
}

public class GenericTreeExample {
    public static void traverse(TreeNode node) {
        if (node != null) {
            System.out.println(node.value);
            for (TreeNode child : node.children){
                traverse(child);
            }
        }
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode("A");
        TreeNode childOne = new TreeNode("B");
        TreeNode childTwo = new TreeNode("C");

        root.addChild(childOne);
        root.addChild(childTwo);

        childOne.addChild(new TreeNode("D"));
        childOne.addChild(new TreeNode("E"));

        childTwo.addChild(new TreeNode("F"));
        childTwo.addChild(new TreeNode("G"));

        System.out.println("Generic Tree Traversal");
        traverse(root);
    }
}