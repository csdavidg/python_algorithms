class Value:
    def __init__(self, e):
        self.value = e

    def __str__(self):
        return str(self.value)

    def eval(self):
        return self.value


class Expression:
    def __init__(self, func, left, right):
        self.func = func
        self.left = left
        self.right = right

    def __str__(self):
        return '({} {} {})'.format(self.left, self.func.__doc__, self.right)

    def eval(self):
        return self.func(self.left.eval(), self.right.eval())


def add(left, right):
    """+"""
    return left + right


def mult(left, right):
    """*"""
    return left * right

# Recursive call of expressions


"""
To evaluate m, there could be up to two recursive calls, one on the left and right sub-expressions, respectively.
In this case, the left sub-expression, a = (1 + 5) is evaluated recursively, while the right sub-expression, 9, is not.
The final computation of 54 is returned as the final result. This example demonstrates the usefulness of the Expression recursive binary tree data structure.
It also shows that recursive implementations are brief and elegant.
"""
a = Expression(add, Value(1), Value(5))
m = Expression(mult, a, Value(9))
print(m, '=', m.eval())
# ((1 + 5) * 9) = 54


# Binary Trees

# Standard structure of a node for a binary tree
"""
class BinaryNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
"""

# Structure required for a AVL balanced tree, each node must store the height


class BinaryNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        self.height = 0

    def height_difference(self):
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1
        return left_height - right_height

    def compute_height(self):
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1
        self.height = 1 + max(left_height, right_height)


class BinaryTree:
    def __init__(self):
        self.root = None

    def rotate_left_right(node):
        child = node.left
        new_root = child.right
        grand1  = new_root.left
        grand2  = new_root.right
        child.right = grand1
        node.left = grand2
        new_root.left = child
        new_root.right = node

        child.compute_height()
        node.compute_height()
        return new_root

    def resolve_left_leaning(node):
        if node.height_difference() == 2:
            if node.left.height_difference() >= 0:
                node = rotate_right(node)##Check book repository for this function
            else:
                node = rotate_left_right(node)##Check book repository for this function
        return node

    def resolve_right_leaning(node):
        if node.height_difference() == -2:
            if node.right.height_difference() <= 0:
                node = rotate_left(node)##Check book repository for this function
            else:
                node = rotate_right_left(node)##Check book repository for this function
        return node

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if node is None:
            return BinaryNode(val)

        if val <= node.value:
            node.left = self._insert(node.left, val)
            node = resolve_left_leaning(node)
        else:
            node.right = self._insert(node.right, val)
            node = resolve_right_leaning(node)

        node.compute_height()  # Compute the height for the new node. Value used by the AVL tree
        return node

    def __contains__(self, target):
        node = self.root
        while node:
            if target == node.value:
                return True

            if target < node.value:
                node = node.left
            else:
                node = node.right

        return False

    def _remove_min(self, node):
        if node.left is None:
            return node.right

        node.left = self._remove_min(node.left)
        node = resolve_right_leaning(node)
        node.compute_height()
        return node

    def remove(self, val):
        self.root = self._remove(self.root, val)

    def _remove(self, node, val):
        if node is None:
            return None

        if val < node.value:
            node.left = self._remove(node.left, val)
            node = resolve_right_leaning(node)
        elif val > node.value:
            node.right = self._remove(node.right, val)
            node = resolve_left_leaning(node)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            original = node
            node = node.right
            while node.left:
                node = node.left

            node.right = self._remove_min(original.right)
            node.left = original.left
            node = resolve_left_leaning(node)

        return node

    def __iter__(self):
        for v in self._inorder(self.root):
            yield v

    def _inorder(self, node):
        if node is None:
            return

        for v in self._inorder(node.left):
            yield v

        yield node.value

        for v in self._inorder(node.right):
            yield v

    