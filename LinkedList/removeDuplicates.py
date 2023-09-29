class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def print_all(self):
        if self.length == 0:
            print("Head: None")
        else:
            print("Head: ", self.head.value)
        print("Length: ", self.length)
        print("\nLinked List:")
        if self.length == 0:
            print("empty")
        else:
            self.print_list()

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1

    # this linkedlist doesn't have tail
    def remove_duplicates(self):
        if self.length == 0:
            return None

        current = self.head
        unique_values = set()  # Use a set to track unique values

        # The first node is always unique, so we add it to the set
        unique_values.add(current.value)

        while current.next:
            if current.next.value in unique_values:
                # Skip the duplicate node
                current.next = current.next.next
                self.length -=1
            else:
                # If the value is not a duplicate, add it to the set
                unique_values.add(current.next.value)
                current = current.next

        return True


my_linked_list = LinkedList(1)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.append(4)
my_linked_list.remove_duplicates()

my_linked_list.print_all()

"""
    EXPECTED OUTPUT:
    ----------------
    Head:  1
    Length:  4
    Linked List:
    1
    2
    3
    4

"""
