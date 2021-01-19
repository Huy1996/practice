class node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

    def __del__(self):
        del self

class search_tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __init__(self, data):
        self.root = node(data)
        self.size = 1

    def insert(self, data):
        if self.root is None:
            self.root = node(data)
        else:
            self.insert(self.root, data)

    def insert_recursively(self, root, data):
        if root.data == data:
            root.data = data
        elif root.data < data:
            if root.right is None:
                root.right = node(data)
            else:
                self.insert_recursively(root.right, data)
        else:
            if root.left is None:
                root.left = node(data)
            else:
                self.insert_recursively(root.left, data)


if __name__ == "__main__":
    pass