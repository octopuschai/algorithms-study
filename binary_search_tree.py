""" binary search tree """


class TreeNode(object):
    def __init__(self, data=None):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def is_leaf(self, ):
        """ self is a leaf node """
        return not (self.left or self.right)

    def is_left_child(self, ):
        """ self is parent's left child """
        return self.parent and self.parent.left == self

    def is_right_child(self, ):
        """ self is parent's right child """
        return self.parent and self.parent.right == self

    def __iter__(self, ):
        """ make tree node iterable, mid-traverse tree """
        if self:
            if self.left:
                for node in self.left:
                    yield node
            yield self.data
            if self.right:
                for node in self.right:
                    yield node


class BinarySearchTree(object):
    def __init__(self, ):
        self.root = None
        self.size = 0

    def insert(self, value):
        """ insert a node with value """
        new_node = TreeNode(value)
        if self.size == 0:
            self.root = new_node
        else:
            n = self.root
            while n:
                p = n
                if value <= n.data:
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
        """ return node with value or None """
        n = self.root
        while n:
            if value == n.data:
                return n
            elif value < n.data:
                n = n.left
            else:
                n = n.right

    def delete(self, value):
        """ delete a node with value """
        node = self.get(value)
        if not node:
            raise ValueError(f'Error, {value} is not in tree.')
        if node.is_leaf():  # node is a leaf node
            if node.is_left_child():
                node.parent.left = None
            if node.is_right_child():
                node.parent.right = None
        elif node.left is None:  # node has only right child
            if node.is_left_child():
                node.right.parent = node.parent
                node.parent.right = node.right
            elif node.is_right_child():
                node.right.parent = node.parent
                node.parent.left = node.right
            else:  # node.parent is None, node is root node
                node.right.parent = None
                self.root = node.right
        elif node.right is None:  # node has only left child
            if node.is_left_child():
                node.left.parent = node.parent
                node.parent.left = node.left
            elif node.is_right_child():
                node.left.parent = node.parent
                node.parent.right = node.left
            else:  # node.parent is None, node is root node
                node.left.parent = None
                self.root = node.left
        else:  # node have two children
            replace_node = self.find_next(node)
            node.data = replace_node.data
            # replace_node.delete()
            if replace_node.is_leaf():  # replace_node is a leaf node
                if replace_node.is_left_child():
                    replace_node.parent.left = None
                if replace_node.is_right_child():
                    replace_node.parent.right = None
            else:  # replace_node has only left child
                if replace_node.is_left_child():
                    replace_node.left.parent = replace_node.parent
                    replace_node.parent.left = replace_node.left
                elif replace_node.is_right_child():
                    replace_node.left.parent = replace_node.parent
                    replace_node.parent.right = replace_node.left
                else:  # replace_node.parent is None, node is root node
                    replace_node.left.parent = None
                    self.root = replace_node.left
        self.size -= 1

    def find_next(self, curr_node):
        """ find next node which has second bigger value than curr_node"""
        n = curr_node.left
        while n.right:
            n = n.right
        return n

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

    def __len__(self, ):
        return self.size

    def __repr__(self, ):
        seq = []
        self.traverse(self.root, seq)
        return ','.join(map(str, seq))
