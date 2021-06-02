"""Module contains class that represent binary tree"""


class BinaryTree:
    """Binary tree representing class"""
    def __init__(self, val=None):
        """Constructor"""
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        """adds new value to the tree"""
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BinaryTree(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BinaryTree(val)

    def get_min(self):
        """searches for minimum value in the three"""
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        """searches for maximum value in the three"""
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def delete(self, val):
        """deletes value from the tree by value"""
        if self is None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def exists(self, val):
        """checks whether this value present in tree or not"""
        if val == self.val:
            return True

        if val < self.val:
            if self.left is None:
                return False
            return self.left.exists(val)

        if self.right is None:
            return False
        return self.right.exists(val)

    def inorder(self, vals):
        """orders values in three from min to max"""
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def find(self, value):
        """find a node in tree by value"""
        node = self
        while node:
            if value < node.val:
                node = node.left
            elif value > node.val:
                node = node.right
            else:
                return node


if __name__ == "__main__":
    binary_tree = BinaryTree()
    binary_tree.insert(56)
    binary_tree.insert(26)
    binary_tree.insert(2)
    binary_tree.insert(103)
    binary_tree.insert(-1)
    binary_tree.insert(2)
    print(binary_tree.inorder([]))
    print(binary_tree.find(2).left.val)
    binary_tree.delete(26)
    print(binary_tree.inorder([]))