from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")

def level_order_traversal(root):
    if not root:
        return
    
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def insert(root, value):
    if not root:
        return Node(value)
    
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if not node.left:
            node.left = Node(value)
            break
        else:
            queue.append(node.left)
        if not node.right:
            node.right = Node(value)
            break
        else:
            queue.append(node.right)
    return root

def search(root, key):
    if not root:
        return False
    
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.value == key:
            return True
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return False

def delete(root, key):
    if not root:
        return None
    
    if root.left is None and root.right is None:
        if root.value == key:
            return None
        else:
            return root
    
    queue = deque([root])
    key_node = None
    last_node = None
    while queue:
        last_node = queue.popleft()
        if last_node.value == key:
            key_node = last_node
        if last_node.left:
            queue.append(last_node.left)
        if last_node.right:
            queue.append(last_node.right)
    
    if key_node:
        key_node.value = last_node.value
        delete_deepest(root, last_node)
    
    return root

def delete_deepest(root, d_node):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is d_node:
            node = None
            return
        if node.right:
            if node.right is d_node:
                node.right = None
                return
            else:
                queue.append(node.right)
        if node.left:
            if node.left is d_node:
                node.left = None
                return
            else:
                queue.append(node.left)

def height(root):
    if not root:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    return max(left_height, right_height) + 1

def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def is_balanced(root):
    def check_height(node):
        if not node:
            return 0
        left_height = check_height(node.left)
        if left_height == -1:
            return -1
        right_height = check_height(node.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1
    return check_height(root) != -1

bt = BinaryTree()
bt.root = Node(1)
insert(bt.root, 2)
insert(bt.root, 3)
insert(bt.root, 4)
insert(bt.root, 5)

print("Inorder Traversal:")
inorder_traversal(bt.root)
print("\nPreorder Traversal:")
preorder_traversal(bt.root)
print("\nPostorder Traversal:")
postorder_traversal(bt.root)
print("\nLevel Order Traversal:")
level_order_traversal(bt.root)
print("\nHeight of Tree:", height(bt.root))
print("Total Nodes:", count_nodes(bt.root))
print("Is Balanced:", is_balanced(bt.root))
print("Search 4:", search(bt.root, 4))
print("Search 10:", search(bt.root, 10))

delete(bt.root, 3)
print("Level Order Traversal After Deletion of 3:")
level_order_traversal(bt.root)