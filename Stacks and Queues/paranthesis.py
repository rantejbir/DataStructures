class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None


def is_balanced_parentheses(input_str):
    stack = Stack()

    for char in input_str:
        if char == "(":
            stack.push("(")
        elif char == ")":
            if stack.is_empty():
                return False  # Unmatched closing parenthesis
            stack.pop()

    return stack.is_empty()


# Example usage:
balanced = is_balanced_parentheses("((()))")
print(balanced)  # True

unbalanced = is_balanced_parentheses("(()))")
print(unbalanced)  # False

unbalanced2 = is_balanced_parentheses(")(")
print(unbalanced2)  # False
