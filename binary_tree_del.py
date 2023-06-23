class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, current_node):
        if data < current_node.data:
            if current_node.left:
                self._insert_recursive(data, current_node.left)
            else:
                current_node.left = Node(data)
        elif data > current_node.data:
            if current_node.right:
                self._insert_recursive(data, current_node.right)
            else:
                current_node.right = Node(data)

    def delete(self, data):
        self.root = self._delete_recursive(data, self.root)

    def _delete_recursive(self, data, current_node):
        if not current_node:
            return current_node

        if data < current_node.data:
            current_node.left = self._delete_recursive(data, current_node.left)
        elif data > current_node.data:
            current_node.right = self._delete_recursive(data, current_node.right)
        else:
            if not current_node.left:
                return current_node.right
            elif not current_node.right:
                return current_node.left
            else:
                temp = self._find_minimum(current_node.right)
                current_node.data = temp.data
                current_node.right = self._delete_recursive(temp.data, current_node.right)

        return current_node

    def _find_minimum(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node

    def pre_order_traversal(self, node):
        if node:
            print(node.data)
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

# Sample usage
binary_tree = BinaryTree()
binary_tree.insert(5)
binary_tree.insert(3)
binary_tree.insert(7)
binary_tree.insert(2)
binary_tree.insert(4)

binary_tree.delete(3)
print("Pre-order Traversal after deletion:")
binary_tree.pre_order_traversal(binary_tree.root)
