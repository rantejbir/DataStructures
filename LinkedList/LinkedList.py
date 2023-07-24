class Node:
    def __init__(self, value):
        # this class will create a new node with a value that is passed
        # and the node will point to next value that will be none and
        # will make it last node of the linked list.
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        # create new node
        # add node to last
        new_node = Node(value)
        # if list is empty
        if self.head is None:
            # it will create a new node and point head and tail to same node
            # as it only points to same node as it is only element inside it
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

    def prepend(self, value):
        # create new node
        # add node to beginning
        pass

    def insert(self, value):
        # create new node
        # insert new node
        pass

    def print_list(self):
        temp = self.head
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

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)
