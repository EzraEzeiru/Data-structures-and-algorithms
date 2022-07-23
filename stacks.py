from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
       cur = self.container.pop()
       return cur

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return self.container == 0

    def size_of_container(self):
        return len(self.container)

    def add_string(self, string):
        for char in string:
            self.push(char)

    def reverse_string(self, string):
        for char in string[::-1]:
            self.push(char)
        return "".join(self.container)

    def is_balanced(self, string):
        i = 0
        if len(string) == 0:
            return False
        while i < len(string):
            j = i + 1
            if string[i] == "{" or string[i] == "[" or string[i] == "(":
                check_char = True
                while check_char:
                    if j == len(string):
                        return False
                    if string[i] + string[j] == "()" or string[i] + string[j] == "[]" or string[i] + string[j] == "{}":
                        i += 1
                        string.strip(string[j])
                        print(string)
                        break
                    else:
                        j += 1
            else:
                i += 1
        return True
s = Stack()

print(s.is_balanced("{{}"))
