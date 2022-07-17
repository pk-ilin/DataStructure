class Stack:
    def __init__(self):
        self.items = []
        self._size = 0

    def push(self, item):
        self.items.append(item)
        self._size += 1

    def pop(self):
        if not self.is_empty():
            self._size -= 1
            return self.items.pop()
        else:
            raise Exception("stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[self._size - 1]
        else:
            raise Exception("stack is empty")

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0
