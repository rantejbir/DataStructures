class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        print("____________")
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.top is None:
            return False
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
        self.height -= 1
        return temp.value


my_stack = Stack(3)
my_stack.print_stack()
my_stack.push(2)
my_stack.push(7)
my_stack.print_stack()
print("pop: ", my_stack.pop())
my_stack.print_stack()
