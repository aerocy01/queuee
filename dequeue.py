class Deque:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def add_front(self, item):
        new_node = Node(item)
        if self.front is None:
            self.front = self.rear = new_node
            return
        new_node.next = self.front
        self.front = new_node

    def add_rear(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def remove_front(self):
        if self.is_empty():
            raise IndexError("Remove front from empty deque")
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("Remove rear from empty deque")
        temp = self.front
        if temp.next is None:
            self.front = self.rear = None
            return temp.data
        while temp.next.next:
            temp = temp.next
        result = temp.next.data
        temp.next = None
        self.rear = temp
        return result

    def display(self):
        elements = []
        temp = self.front
        while temp:
            elements.append(temp.data)
            temp = temp.next
        return elements
