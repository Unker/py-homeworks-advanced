from copy import deepcopy


class Stack:
    def __init__(self, inputs: list):
        if isinstance(inputs, list):
            self.vals = deepcopy(inputs)
        elif isinstance(inputs, str):
            self.vals = [char for char in inputs]
        else:
            self.vals = [inputs]
        self.sz = len(self.vals)

    def size(self) -> int:
        return self.sz

    def is_empty(self):
        return self.sz == 0

    def push(self, element):
        self.vals.append(element)
        self.sz += 1

    def pop(self):
        if self.is_empty():
            raise ValueError('The stack is empty')
        else:
            ret = self.vals.pop()
            self.sz -= 1
        return ret

    def peek(self):
        if self.is_empty():
            raise ValueError('The stack is empty')
        else:
            return self.vals[-1]

    def __str__(self):
        return f'Stack: {self.vals}'

    def __iter__(self):
        return self

    def __next__(self):
        if self.size():
            return self.pop()
        else:
            raise StopIteration

    def __eq__(self, other):
        return set(self.vals) == set(other.vals)

    def __len__(self):
        return self.size()


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    stack = Stack(a)
    stack2 = Stack(a)
    print(stack)
    print(stack.size())
    print(stack.is_empty())
    print(f'eq: {stack==stack2}')
    stack.pop()
    print(f'eq: {stack==stack2}')
    for element in stack:
        print(element)
