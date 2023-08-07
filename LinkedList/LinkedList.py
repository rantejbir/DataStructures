# this class will create a new node with a value that is passed
# and the node will point to next value that will be none and
# will make it last node of the linked list.
class Node:
    def __init__(self, value):

        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def get(self, index):
        if index < 0 or self.head is None:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def append(self, value):
        # create new node
        # add node to last
        # it will create a new node and point
        # head and tail to same node as it only
        # points to same node as it is only element inside it
        new_node = Node(value)
        # if list is empty
        if self.head is None:

            self.head = new_node
            self.tail = new_node
        # if list is not empty
        else:
            # it will create a new node and points tail to new node
            # and its value that has been passed
            self.tail.next = new_node
            self.tail = new_node
        #  it will increase the length of the linkedList
        self.length += 1
        return True

    def pop(self):
        # it will delete an element from the last of the list.
        # for that we need to point tail to previous
        # element and next variable to None that will
        # pop one element from the end

        # case 1: if list is empty
        if self.head is None:
            return None
        # case 2 if list is not empty
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    def prepend(self, value):
        # create new node
        # add node to beginning
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def insert(self, index, value):
        # create new node
        # insert new node
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)

        if temp:
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = self.get(index)
        temp.next = None
        pre.next = temp.next
        return temp.value

    def pop_first(self):
        # it will remove very first element
        # of the list and return it
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value

    def print_list(self):
        temp = self.head
        print()
        while temp is not None:
            print(temp.value)
            temp = temp.next


#  All functions do one same thing that is to create a new node,
#  so we will create a class name node to create that node
my_linked_list = LinkedList(4)
# appending new elements in the List
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.append(1)
my_linked_list.print_list()
my_linked_list.remove(1)

my_linked_list.print_list()
print()

print(my_linked_list.pop())
print(my_linked_list.get(2))

my_linked_list.prepend(109)
my_linked_list.print_list()
print()
print(my_linked_list.pop_first())
print()

my_linked_list.print_list()
