class Node:
    def __init__(self, val, rest=None):
        self.value = val
        self.next = rest


def sum_iterative(n):
    total = 0
    while n:
        total += n.value
        n = n.next
    return total


def sum_list(n):
    if n is None:
        return 0
    return n.value + sum_list(n.next)


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, val):
        self.top = Node(val, self.top)

    def pop(self):
        if self.is_empty():
            raise RuntimeError('Stack is empty')

        val = self.top.value
        self.top = self.top.next
        return val
