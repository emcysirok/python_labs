from collections import deque

class Stack:
    def __init__(self):
        self._data = []
    def push(self, item):
        self._data.append(item)
    def pop(self):
        if self.is_empty():
            raise IndexError
        return self._data.pop()
    def peek(self):
        if self.is_empty():
            return None
        return self._data[-1]
    def is_empty(self):
        return len(self._data) == 0
    def __len__(self):
        return len(self._data)
    def __str__(self):
        return f"Stack({self._data})"

class Queue:
    def __init__(self):
        self._data = deque()
    def enqueue(self, item):
        self._data.append(item)
    def dequeue(self):
        if self.is_empty():
            raise IndexError
        return self._data.popleft()
    def peek(self): 
        if self.is_empty():
            return None
        return self._data[0]
    def is_empty(self):
        return len(self._data) == 0
    def __len__(self):
        return len(self._data)
    def __str__(self):
        return f"Queue({list(self._data)})"

if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print(s)
    print(f"peek: {s.peek()}")
    print(f"pop: {s.pop()}")
    print(s)
    print() 
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    print(q)
    print(f"peek: {q.peek()}")
    print(f"dequeue: {q.dequeue()}")
    print(q)