
class IndexedMinPQ:

    def less(self, i, j):
        return self.priorities[i] > self.priorities[j]

    def swap(self, i, j):
        self.values[i], self.values[j] = self.values[j], self.values[i]
        self.priorities[i], self.priorities[j] = self.priorities[j], self.priorities[i]

        self.location[self.values[i]] = i
        self.location[self.values[j]] = j

    def __init__(self, size):
        self.N = 0
        self.size = size
        self.values = [None] * (size+1)
        self.priorities = [None] * (size+1)

        self.location = {}

    def __contains__(self, v):
        return v in self.location

    def enqueue(self, v, p):
        self.N += 1

        self.values[self.N], self.priorities[self.N] = v, p
        self.location[v] = self.N
        self.swim(self.N)

    def sink(self, parent):
        while 2*parent <= self.N:
            child = 2*parent
            if child < self.N and self.less(child, child+1):
                child += 1
            if not self.less(parent, child):
                break
            self.swap(child, parent)
            parent = child

    def swim(self, child):
        while child > 1 and self.less(child//2, child):
            self.swap(child, child//2)
            child = child // 2

    def decrease_priority(self, v, lower_priority):
        idx = self.location[v]
        if lower_priority >= self.priorities[idx]:
            raise RuntimeError(
                'You can not use a higher priority than the existing one for the node')

        self.priorities[idx] = lower_priority
        self.swim(idx)

    def dequeue(self):
        min_value = self.values[1]

        self.values[1] = self.values[self.N]
        self.priorities[1] = self.priorities[self.N]
        self.location[self.values[1]] = 1

        self.values[self.N] = self.priorities[self.N] = None
        self.location.pop(min_value)

        self.N -= 1
        self.sink(1)
        return min_value

    def is_empty(self):
        return self.N == 0
