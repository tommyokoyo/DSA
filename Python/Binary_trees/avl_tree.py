# AVL Tree is a self-balancing BST where the heights of two child subtrees differ by at most one
# Rotations are used to maintain this property

class AVLnode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
    
def get_height(node):
    return node.height if node else 0

def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0

def right_rotate(node):
    newparentnode = node.left
    T2 = newparentnode.right

    newparentnode.right = node
    node.left = T2

    node.height = 1 + max(get_height(node.left), get_height(node.right))
    newparentnode.height = 1 + max(get_height(newparentnode.left), get_height(newparentnode.right))

    return newparentnode

def left_rotate(node):
    newparentnode = node.right
    T2 = newparentnode.left
    newparentnode.left = node
    node.right = T2
    node.height = 1 + max(get_height(node.left), get_height(node.right))
    newparentnode.height = 1 + max(get_height(newparentnode.left), get_height(newparentnode.right))
    return newparentnode

def avl_insert(node, key):
    if not node:
        return AVLnode(key)
    if key < node.key:
        node.left = avl_insert(node.left, key)
    else:
        node.right = avl_insert(node.right, key)
    
    node.height = 1 + max(get_height(node.left), get_height(node.right))
    balance = get_balance(node)

    if balance > 1 and key < node.left.key:
        return right_rotate(node)
    
    if balance < -1 and key > node.right.key:
        return left_rotate(node)
    
    if balance > 1 and key > node.left.key:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    
    if balance < -1 and key < node.right.key:
        node.right = right_rotate(node.right)
        return left_rotate(node)
    
    return node

def pre_order(node):
    if not node:
        return
    print(node.key, end=' ')
    pre_order(node.left)
    pre_order(node.right)

# usage example
root_avl = None
for key in [10, 20, 30, 40, 50, 25]:
    root_avl = avl_insert(root_avl, key)
print("\n AVL pre-order traversal")
pre_order(root_avl)
