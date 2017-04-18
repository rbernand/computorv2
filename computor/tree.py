class Node:
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right

    @classmethod
    def empty(cls, value):
        return cls(None, None, None)

    @property
    def depth(self):
        if self.left and self.right:
            return max(self.left.depth, self.right.depth) + 1
        elif self.left:
            return self.left.depth + 1
        elif self.right:
            return self.right.depth + 1
        return 1

    @property
    def size(self):
        if self.left and self.right:
            return 1 + self.left.size + self.right.size
        elif self.left:
            return 1 + self.left.size
        elif self.right:
            return 1 + self.right.size
        return 1

    def tostr(self):
        return "Node: %s" % id(self)

    def print_tree(self, sep="--", _depth=0):
        if _depth == 0:
            print("")
        fmt = "|%s %s"
        print(fmt % (sep * _depth, self.tostr()))
        if self.left:
            self.left.print_tree(_depth=_depth + 1)
        if self.right:
            self.right.print_tree(_depth=_depth + 1)

    def get_root(self):
        if self.parent is None:
            return self
        return self.parent.get_root()
