class Node:
    """Node class for a binary search tree (BST). Each node has a value, and references to left and right child nodes."""
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    """Binary search tree class. Supports insert and search operations."""
    def __init__(self):
        self.root = None  # Initially, the tree is empty

    def insert(self, key):
        """Insert a new element into the BST."""
        if self.root is None:
            self.root = Node(key)  # If tree is empty, the new element becomes the root
        else:
            self._insert_recursive(self.root, key)  # Otherwise, insert it in the correct position

    def _insert_recursive(self, node, key):
        """Helper method to insert a new element into the BST recursively."""
        if key < node.val:
            # Insert in the left subtree
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            # Insert in the right subtree
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        """Search for an element in the BST."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        """Helper method to search for an element in the BST recursively."""
        if node is None or node.val == key:
            return node  # Element found or not in the tree
        if key < node.val:
            return self._search_recursive(node.left, key)  # Search in the left subtree
        return self._search_recursive(node.right, key)  # Search in the right subtree

    def in_order_traversal(self):
        """Perform in-order traversal of the BST and print elements."""
        self._in_order_recursive(self.root)

    def _in_order_recursive(self, node):
        """Helper method for in-order traversal of the BST."""
        if node is not None:
            self._in_order_recursive(node.left)
            print(node.val, end=' ')  # Print the node value
            self._in_order_recursive(node.right)

# Example usage
bst = BinarySearchTree()
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(5)

bst.in_order_traversal()  # should print 1 3 5 7 in sorted order
print("\nSearch for 5:", "Found" if bst.search(5) else "Not Found")
