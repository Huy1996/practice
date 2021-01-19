from data-structure.linked-list.sort import sort
class node(object):
    def __init__(self, data = None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def __del__(self):
        del self.data

class forward_linked_list(object):
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.current = None
        self.__size = 0

    def __init__(self, data):
        input = node(data)
        self.__head = input
        self.__tail = input
        self.current = None
        self.__size = 1

    def __del__(self):
        if self.__head is not None:
            delete = self.__head
            current = self.__head
            while current is not None:
                current = current.next
                del delete
                delete = current
        del self.__size

    def insert_front(self, data):
        input = node(data)
        if self.__head is None:
            self.__head = input
            self.__tail = input
            self.__size = 1
        else:
            input.next = self.__head
            self.__head = input
            self.__size += 1

    def insert_back(self, data):
        input = node(data)
        if self.__head is None:
            self.__head = input
            self.__tail = input
            self.__size = 1
        else:
            self.__tail.next = input
            self.__tail = input
            self.__size += 1

    def __travel_to(self, pos):
        self.current = self.__head
        for i in range(pos):
            self.current = self.current.next

    def insert_at(self, data, pos: int):
        if pos > self.__size:
            raise Exception('Invalid position.')
        elif pos == 0:
            self.insert_front(data)
        elif pos == self.__size:
            self.insert_back(data)
        else:
            input = node(data)
            self.__travel_to(pos - 1)
            input.next = self.current.next
            self.current.next = input
            self.__size += 1

    def delete___head(self):
        if self.__size == 1:
            delete = self.__head
            self.__head = None
            self.__tail = None
            del delete
            self.__size -= 1
        elif self.__size == 0:
            raise Exception('Empty linked list.')
        else:
            delete = self.__head
            self.__head = self.__head.next
            del delete
            self.__size -= 1

    def delete_back(self):
        if self.__size == 1:
            delete = self.__head
            self.__head = None
            self.__tail = None
            del delete
            self.__size -= 1
        elif self.__size == 0:
            raise Exception('Empty linked list.')
        else:
            delete = self.__tail
            self.__travel_to(self.__size - 1)
            self.__tail = self.current
            self.__tail.next = None
            del delete
            self.__size -= 1

    def delete_at(self, pos):
        if pos >= self.__size:
            raise Exception('Invalid position.')
        elif pos == 0:
            self.delete___head()
        elif pos == self.__size - 1:
            self.delete_back()
        else:
            self.__travel_to(pos - 1)
            delete = self.current.next
            self.current.next = self.current.next.next
            del delete
            self.__size -= 1

    def at(self, pos):
        if pos >= self.__size:
            raise Exception('Invalid position.')
        else:
            self.__travel_to(pos)
            return self.current.data

    def top(self):
        return self.__head.data

    def bottom(self):
        return self.__tail.data

    def search(self, data):
        self.current = self.__head
        while self.current is not None:
            if self.current.data == data:
                return self.current.data
            self.current = self.current.next
        return None




if __name__ == "__main__":
    fun = forward_linked_list(5)
    fun.insert_back(6)
    fun.insert_front(1)
    print(fun.__head, " ", fun.__head.next, " ", fun.__head.next.next, fun.__size)
    fun.insert_at(4,2)
    print(fun.__head, " ", fun.__head.next, " ", fun.__head.next.next, " ", fun.__head.next.next.next, fun.__size)
    try:
        fun.at(10)
    except Exception:
        print('invalid call')

    print(fun.__head, " ", fun.__head.next, " ", fun.__head.next.next, fun.__size)
