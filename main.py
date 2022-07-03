class Stack:
    def __init__(self, stack: str):
        self.stack = stack

    def is_empty(self):
        if len(self.stack) == 0:
            return False
        else:
            return True

    def push(self, new_element: str):
        self.stack = self.stack + new_element

    def pop(self):
        result = self.stack[-1]
        self.stack.replace(self.stack[-1], "")
        return result

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


