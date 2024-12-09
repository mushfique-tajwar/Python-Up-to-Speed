class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    def insert(self, root, key):
        # Perform normal BST insertion
        if not root:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # Duplicate keys not allowed

        # Update height of this ancestor node
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        # Get balance factor
        balance = self.get_balance(root)

        # Rebalance the tree
        if balance > 1 and key < root.left.key:  # Left Left
            return self.right_rotate(root)
        if balance < -1 and key > root.right.key:  # Right Right
            return self.left_rotate(root)
        if balance > 1 and key > root.left.key:  # Left Right
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:  # Right Left
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, key):
        if not root:
            return root

        # Perform standard BST delete
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        # Update height
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        # Get balance factor
        balance = self.get_balance(root)

        # Rebalance the tree
        if balance > 1 and self.get_balance(root.left) >= 0:  # Left Left
            return self.right_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:  # Left Right
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:  # Right Right
            return self.left_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:  # Right Left
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    def pre_order(self, root):
        if root:
            print(root.key, end=" ")
            self.pre_order(root.left)
            self.pre_order(root.right)


# Driver Program
if __name__ == "__main__":
    avl = AVLTree()
    root = None

    # Insert elements
    elements = [10, 20, 30, 40, 50, 25]
    for elem in elements:
        root = avl.insert(root, elem)

    print("Preorder traversal after insertion:")
    avl.pre_order(root)
    print()

    # Delete elements
    root = avl.delete(root, 50)
    print("Preorder traversal after deletion of 50:")
    avl.pre_order(root)
    print()