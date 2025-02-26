# This a binary tree with an ordering property: 
# for each node, all keys in the left subtree are smaller, 
# and all keys in the right subtree are larger

# real-world use case: Databases in memory data indexing and search applicatons

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.rightvalue = None
        self.leftvalue = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = BSTNode(value)
        else:
            self._insert(self.root, value)
    
    def _insert(self, node, value):
        if value < node.value:
            if node.leftvalue:
                self._insert(node.leftvalue, value)
            else:
                node.leftvalue = BSTNode(value)
        else:
            if node.rightvalue:
                self._insert(node.rightvalue, value)
            else:
                node.rightvalue = BSTNode(value)
    
    def search(self, value):
        return self._search(self.root, value)
    
    def _search(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search(node.leftvalue, value)
        else:
            return self._search(node.rightvalue, value)
        
# usage
bst = BST()
for val in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    bst.insert(val)

print("\nBST search results")
print(f"search for {bst.search(7)}")
print(f"search for {bst.search(3)}")
