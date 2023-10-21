class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if value == temp.value:
                return True
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
        return False

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right



tree = BinarySearchTree()
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(21)
tree.insert(12)
tree.insert(33)

print(tree.root.value)
print(tree.root.left.value)
print(tree.root.right.value)

print(tree.contains(11))
