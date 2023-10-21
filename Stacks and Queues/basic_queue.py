class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        print("____________")
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first, self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.first is None:
            return False
        temp = self.first
        if self.length == 1:
            self.first, self.last = None
        else:
            self.first = self.first.next
        self.length -= 1
        return temp.value


my_queue = Queue(5)
my_queue.print_queue()
my_queue.enqueue(8)
my_queue.print_queue()
my_queue.enqueue(82)
my_queue.print_queue()
print("pop: ", my_queue.dequeue())
my_queue.print_queue()
print("pop: ", my_queue.dequeue())
my_queue.print_queue()
