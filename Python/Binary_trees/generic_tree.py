# Generic tree represents hierarchical where each node can have
# an arbitary number of children

# Real-world use case: File systems directories (Nodes) contains files and subdirectories (children)

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, node):
        self.children.append(node)

def traverse_tree(root):
    if root:
        print(f"{root.value}")
        for child in root.children:
            traverse_tree(child)

# usage example
root = TreeNode('A')
firstChild = TreeNode('B')
secondChild = TreeNode('C')
root.add_child(firstChild)
root.add_child(secondChild)
firstChild.add_child(TreeNode('D'))
firstChild.add_child(TreeNode('E'))
secondChild.add_child(TreeNode('F'))
secondChild.add_child(TreeNode('G'))
secondChild.add_child(TreeNode('H'))

print("Tree Traversal")
traverse_tree(root)
