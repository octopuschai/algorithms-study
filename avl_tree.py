""" AVL tree """


class TreeNode(object):
    def __init__(self, data=None):
        self.data = data  # node value
        self.balance_factor = 0  # node balance factor
        self.parent = None  # node parent pointer
        self.left = None  # node left child pointer
        self.right = None  # node right child pointer

    def has_any_children(self, ):
        return self.left or self.right

    def has_both_children(self, ):
        return self.left and self.right

    def has_left_child(self, ):
        return self.left

    def has_right_child(self, ):
        return self.right

    def is_leaf(self, ):
        return not (self.left or self.right)

    def is_left_child(self, ):
        return self.parent and self.parent.left == self

    def is_right_child(self, ):
        return self.parent and self.parent.right == self


class AVL(object):
    def __init__(self, ):
        self.root = None  # root pointer
        self.size = 0  # number of tree nodes in AVL

    def get(self, value):
        pass

    def insert(self, value):
        """ insert a node with value """
        node = TreeNode(value)
        if self.size == 0:
            self.root = node
        else:
            n = self.root
            while n:
                p = n
                if value <= n.data:
                    n = n.left
                    flag = 0
                else:
                    n = n.right
                    flag = 1
            if flag:
                p.right = node
            else:
                p.left = node
            node.parent = p
            self.update_balance_factor(p)

        self.size += 1

    def height(self, node):
        """ return height of node sub-tree """
        h = 0
        if node.has_any_children():
            h = 1 + max(self.height(node.left), self.height(node.right))
        return h

    def update_balance_factor(self, node):
        """ update node balance factor recursively """
        node.balance_factor = self.height(node.left) - self.height(node.right)
        if abs(node.balance_factor) > 1:
            self.rebalance(node)
        if node.parent is not None:
            self.update_balance_factor(node.parent)

    def rebalance(self, node):
        if node.has_left_child():
            if node.left.balance_factor == 1:
                self.rotate_left(node)
            if node.left.balance_factor == -1:
                self.rotate_right(node.left)
                self.rotate_left(node)
        if node.has_right_child():
            if node.right.balance_factor == -1:
                self.rotate_right(node)
            if node.right.balance_factor == 1:
                pass

    def rotate_left(self, node):
        node.left.parent = node.parent
        node.parent.left = node.left
        if node.has_right_child():
            node.parent = node.left
            tmp_node = node.left.right
            node.left.right = node
            node.left = tmp_node
        else:
            node.parent = node.left
            node.left.right = node
            node.left = None

    def rotate_right(self, node):
        node.right.parent = node.parent
        node.parent.right = node.right
        if node.has_left_child():
            node.parent = node.right
            tmp_node = node.right.left
            node.right.left = node
            node.right = tmp_node
        else:
            node.parent = node.right
            node.right.left = node
            node.right = None

    def delete(self, value):
        pass
