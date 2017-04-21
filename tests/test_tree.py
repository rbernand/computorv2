from computor.tree import Node


def test_node():
    t = Node.empty(0)


def test_depth():
    root = Node.empty(0)
    assert root.depth == 1
    root.left = Node.empty(0)
    assert root.depth == 2
    assert root.left.depth == 1
    root.right = Node.empty(0)
    assert root.depth == 2
    root.left.left = Node.empty(0)
    assert root.depth == 3
    assert root.left.depth == 2
    root.print_tree()


def test_size():
    root = Node.empty(0)
    assert root.size == 1
    root.left = Node.empty(0)
    assert root.size == 2
    root.right = Node.empty(0)
    assert root.size == 3
    assert root.left.size == 1
    root.left.left = Node.empty(0)
    assert root.size == 4
    assert root.left.size == 2
    rsoot.print_tree()
