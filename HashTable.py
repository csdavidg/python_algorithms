class Entry:
    def __init__(self, k, v):
        self.key = k
        self.value = v

# First approach
# class Hashtable:
#   def __init__(self, M=10):
#     self.table = [None] * M
#     self.M = M

#   def get(self, k):
#     hc = hash(k) % self.M
#     return self.table[hc].value if self.table[hc] else None

#   def put(self, k, v):
#     hc = hash(k) % self.M
#     entry = self.table[hc]
#     if entry:
#       if entry.key == k:
#         entry.value = v
#       else:
#         raise RuntimeError('Key Collision: {} and {}'.format(k, entry.key))
#     else:
#       self.table[hc] = Entry(k, v)

# Second approach supporting open addressing
# class Hashtable:
#   def __init__(self, M=10):
#     self.table = [None] * M
#     self.M = M
#     self.N = 0

#   def get(self, k):
#     hc = hash(k) % self.M
#     while self.table[hc]:
#       if self.table[hc].key == k:
#         return self.table[hc].value
#       hc = (hc + 1) % self.M
#     return None

#   def put(self, k, v):
#     hc = hash(k) % self.M
#     while self.table[hc]:
#       if self.table[hc].key == k:
#         self.table[hc].value = v
#         return
#       hc = (hc + 1) % self.M

#     if self.N >= self.M - 1:
#       raise RuntimeError ('Table is Full.')

#     self.table[hc] = Entry(k, v)
#     self.N += 1


class LinkedEntry:
    def __init__(self, k, v, rest=None):
        self.key = k
        self.value = v
        self.next = rest


# Third Approac
# h using a LinkedList and separate chaining technique
class Hashtable:
    def remove(self, k):
        hc = hash(k) % self.M
        entry = self.table[hc]
        prev = None
        while entry:
            if entry.key == k:
                if prev:
                    prev.next = entry.next
                else:
                    self.table[hc] = entry.next

                self.N -= 1
                return entry.value

            prev, entry = entry, entry.next

        return None

    def __init__(self, M=10):
        self.table = [None] * M
        self.M = M
        self.N = 0

    def get(self, k):
        hc = hash(k) % self.M
        entry = self.table[hc]
        while entry:
            if entry.key == k:
                return entry.value
            entry = entry.next
        return None

    def put(self, k, v):
        hc = hash(k) % self.M
        entry = self.table[hc]
        while entry:
            if entry.key == k:
                entry.value = v
                return
            entry = entry.next

        self.table[hc] = LinkedEntry(k, v, self.table[hc])
        self.N += 1


table = Hashtable(1000)
table.put('April', 30)
table.put('May', 31)
table.put('September', 30)
table.put('September', 30)

print(table.get('August'))     # Miss: should print None since not present
print(table.get('September'))  # Hit: should print 30
print(hash('rose'))
print(hash('smell'))
