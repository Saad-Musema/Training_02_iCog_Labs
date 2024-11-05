class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        if data < self.data:
            if self.left_child:
                self.left_child.insert(data)
            else:
                self.left_child = Node(data)
        else:
            if self.right_child:
                self.right_child.insert(data)
            else:
                self.right_child = Node(data)

    def print_tree(self):
        if self.left_child:
            self.left_child.print_tree()
        print(self.data, end=' ')
        if self.right_child:
            self.right_child.print_tree()


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            self.root.insert(data)
        else:
            self.root = Node(data)

    def print_tree(self):
        if self.root:
            self.root.print_tree()


tree = Tree()
tree.insert(27)
tree.insert(14)
tree.insert(35)
tree.insert(10)
tree.insert(19)
tree.insert(31)
tree.insert(42)

tree.print_tree()