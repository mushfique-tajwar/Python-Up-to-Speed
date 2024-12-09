class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if key < root.value:
                root.left = self.insert(root.left, key)
            else:
                root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.value == key:
            return root
        elif key < root.value:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.value:
            root.left = self.delete(root.left, key)
        elif key > root.value:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.minValueNode(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value, end=' ')
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.value, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.value, end=' ')

bst = BinarySearchTree()
bst.root = bst.insert(bst.root, 50)
bst.root = bst.insert(bst.root, 30)
bst.root = bst.insert(bst.root, 70)

result = bst.search(bst.root, 30)
if result:
    print("Node found:", result.value)
else:
    print("Node not found")

bst.root = bst.delete(bst.root, 30)

print("In-order Traversal:")
bst.inorder(bst.root)
print("\nPre-order Traversal:")
bst.preorder(bst.root)
print("\nPost-order Traversal:")
bst.postorder(bst.root)

def height(self, root):
    if not root:
        return -1
    left_height = self.height(root.left)
    right_height = self.height(root.right)
    return max(left_height, right_height) + 1

min_node = bst.minValueNode(bst.root)
print("Minimum Value:", min_node.value)

bst2 = BinarySearchTree()
bst2.root = bst2.insert(bst2.root, 50)
bst2.root = bst2.insert(bst2.root, 30)
bst2.root = bst2.insert(bst2.root, 70)
bst2.root = bst2.insert(bst2.root, 20)
bst2.root = bst2.insert(bst2.root, 40)
bst2.root = bst2.insert(bst2.root, 60)
bst2.root = bst2.insert(bst2.root, 80)

print("In-order Traversal:")
bst2.inorder(bst2.root)

bst2.root = bst2.delete(bst2.root, 20)

print("\nIn-order Traversal after deletion:")
bst2.inorder(bst2.root)
