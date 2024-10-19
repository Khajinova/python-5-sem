class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.value))
            current = current.next
        return str(result)

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def pop(self, index=None):
        if self.size == 0:
            raise IndexError("список пуст")
        
        if index is None:
            index = self.size - 1

        if not 0 <= index < self.size:
            raise IndexError("такого индекса нет")

        current = self.head
        if index == 0:
            self.head = current.next
        else:
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1

    def __getitem__(self, index):
        if not 0 <= index < self.size:
            raise IndexError("такого индекса нет")
        current = self.head
        for i in range(index):
            current = current.next
        return current.value

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next


