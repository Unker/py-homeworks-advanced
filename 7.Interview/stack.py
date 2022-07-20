from typing import List


class Stack:
    def __init__(self, vals: list):
        self.vals = vals
        self.sz = len(vals)

    def size(self) -> int:
        return self.sz

    def is_empty(self):
        return self.size == 0

    def push(self, element):
        self.vals.append(element)
        self.sz += 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            ret = self.vals.pop()
            self.sz -= 1
        return ret

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.vals[-1]

    def __str__(self):
        return f'Stack: {self.vals}'

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def __eq__(self, other):
        pass

    def __len__(self):
        return self.size()


if __name__ == '__main__':
    a = [1,2,3,4,5]
    stack = Stack(a)
    print(stack)
    print(stack.size())
    print(stack.is_empty())
