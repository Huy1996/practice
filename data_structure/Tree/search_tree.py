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
    def __init__(self, data=None):
        if data is None:
            self.root = None
            self.size = 0
        else:
            self.root = node(data)
            self.size = 1

    def insert(self, data):
        if self.root is None:
            self.root = node(data)
            self.size += 1
        else:
            self.insert_recursively(self.root, data)

    def insert_recursively(self, root, data):
        if root.data == data:
            root.data = data
        elif root.data < data:
            if root.right is None:
                root.right = node(data)
                self.size += 1
            else:
                self.insert_recursively(root.right, data)
        else:
            if root.left is None:
                root.left = node(data)
                self.size += 1
            else:
                self.insert_recursively(root.left, data)

    def insert_interation(self, data):
        if self.root is None:
            self.root = node(data)
            self.size += 1
        else:
            current = self.root
            input = node(data)
            while True:
                if current.data == data:
                    current.data = data
                    self.size -= 1
                    break
                elif current.data > data:
                    if current.left is None:
                        current.left = input
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = input
                        break
                    current = current.right
            self.size += 1

    def search(self, key):
        if self.root is None:
            return False
        else:
            return self.search_recursively(key, self.root)

    def search_recursively(self, key, root):
        if root.data == key:
            return root
        elif root is None:
            return False
        elif root.data > key:
            return self.search_recursively(key, root.left)
        else:
            return self.search_recursively(key, root.right)

    def search_interation(self, key):
        if self.root is None:
            return False
        else:
            current = self.root
            while current is not None:
                if current.data == key:
                    return current
                elif current.data > key:
                    current = current.left
                else:
                    current = current.right
            return False

    def delete(self, key):
        if self.search_interation(key) is False:
            raise Exception('The data does not exist.')
        else:
            self.root = self.delete_recursively(key, self.root)

    def delete_recursively(self, key, root):
        if root.data == key:
            if root.left is None and root.right is None:
                root = None
                return root
            elif root.left is None and root.right is not None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            else:
                min = self.min_node(root.right)
                root.data = min.data
                root.right = self.delete_recursively(min.data, root.right)
        elif root.data > key:
            root.left = self.delete_recursively(key, root.left)
        elif root.data < key:
            root.right = self.delete_recursively(key, root.right)
        return root


    def min_node(self, root):
        while root.left is not None:
            root = root.left
        return root

if __name__ == "__main__":
    a = search_tree(20)
    b=[10,5,31,28,11]
    for i in b:
        a.insert(i)
    print(a.search_interation(5).data)
