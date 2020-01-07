""" binary search tree """


class TreeNode(object):
    def __init__(self, data=None):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self, ):
        self.root = None
        self.size = 0

    def insert(self, value):
        new_node = TreeNode(value)
        if self.size == 0:
            self.root = new_node
        else:
            n = self.root
            while n:
                p = n
                if value < n.data:
                    flag = 0
                    n = n.left
                else:
                    flag = 1
                    n = n.right
            if flag:
                new_node.parent = p
                p.right = new_node
            else:
                new_node.parent = p
                p.left = new_node
        self.size += 1

    def get(self, value):
        n = self.root
        while n:
            if value == n.data:
                return n
            elif value < n.data:
                n = n.left
            else:
                n = n.right

    def delete(self, value):
        node = self.get(value)
        if not node:
            raise ValueError(f'Error, {value} is not in tree.')
        if not (node.left or node.right):  # node is a leaf node
            if node.is_left_child():
                node.parent.left = None
            if node.is_right_child():
                node.parent.right = None
        elif node.left is None:  # node has only right child
            if node.is_left_child():
                node.right.parent = node.parent
                node.parent.right = node.right
            if node.is_right_child():
                node.right.parent = node.parent
                node.parent.left = node.right
        elif node.right is None:  # node has only left child
            if node.is_left_child():
                node.left.parent = node.parent
                node.parent.left = node.left
            if node.is_right_child():
                node.left.parent = node.parent
                node.parent.right = node.left
        else:  # node have two children
            pass

    def is_left_child(self, ):
        """ self is parent's left child """
        return self.parent and self.parent.left == self

    def is_right_child(self, ):
        """ self is parent's right child """
        return self.parent and self.parent.right == self

    def build(self, seq):
        """ insert node from a seq """
        for item in seq:
            self.insert(item)

    def traverse(self, node, seq):
        """ mid-traverse tree """
        if node is not None:
            self.traverse(node.left, seq)
            seq.append(node.data)
            self.traverse(node.right, seq)

    def __repr__(self, ):
        seq = []
        self.traverse(self.root, seq)
        return ','.join(map(str, seq))
