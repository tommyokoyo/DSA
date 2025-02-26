# Binary tree restricts each node to at most two children (left and right)
# real world use: Representing and evaluating mathematical expressions

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.leftvalue = None
        self.rightvalue = None

def inorder_traveral(node):
    if node:
        inorder_traveral(node.leftvalue)
        print(node.value, end=' ')
        inorder_traveral(node.rightvalue)

# usage example
root = BinaryTreeNode(10)
root.leftvalue = BinaryTreeNode(8)
root.rightvalue = BinaryTreeNode(9)
root.leftvalue.leftvalue = BinaryTreeNode(5)
root.rightvalue.rightvalue = BinaryTreeNode(4)

print("Tree traveral")
inorder_traveral(root)