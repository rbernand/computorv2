class Node:
    def __init__(self, left, right):
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

    def __str__(self):
        return "Node: %s" % id(self)

    def tostr(self, sep="--"):
        def recurse(node, _depth=0):
            yield fmt % (sep * _depth, str(node))
            if node.left:
                yield from recurse(node.left, _depth + 1)
            if node.right:
                yield from recurse(node.right, _depth + 1)
        fmt = "|%s %s"
        return "\n".join(recurse(self))
