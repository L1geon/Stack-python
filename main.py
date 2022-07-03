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

    def balanced(self):
        open_list = ["[", "{", "("]
        close_list = ["]", "}", ")"]
        stack = []
        for i in self.stack:
            if i in open_list:
                stack.append(i)
            elif i in close_list:
                ind = close_list.index(i)
                if ((len(stack) > 0) and (open_list[ind] == stack[len(stack) - 1])):
                    stack.pop()
                else:
                    return "Несбалансированно"
        if len(stack) == 0:
            return "Сбалансированно"


d = Stack("{}{}")
print(d.balanced())
