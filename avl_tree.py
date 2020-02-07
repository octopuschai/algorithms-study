""" AVL tree """


class TreeNode(object):
    def __init__(self, data=None):
        self.data = data  # node value
        self.balance_factor = 0  # node balance factor
        # value 0 means left sub-tree-height equal right sub-tree-height
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
        if node is not None:
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
        """ adjust node balance factor """
        if node.balance_factor > 0:
            if node.left.balance_factor > 0:
                self.rotate_left(node)
            else:
                self.rotate_right(node.left)
                self.rotate_left(node)
        else:
            if node.right.balance_factor < 0:
                self.rotate_right(node)
            else:
                self.rotate_left(node.right)
                self.rotate_left(node)

    def rotate_left(self, node):
        new_node = node.left
        new_height = self.height(new_node)
        new_r_height = self.height(new_node.right)
        node.left.parent = node.parent
        if self.root == node:  # node is root node
            self.root = node.left
        else:
            if node.is_left_child():
                node.parent.left = node.left
            else:
                node.parent.right = node.left
        if node.has_right_child():
            node.parent = node.left
            tmp_node = node.left.right
            node.left.right = node
            node.left = tmp_node
        else:
            node.parent = node.left
            node.left.right = node
            node.left = None
        # new_node.balance_factor -= 1
        # node.balance_factor = max(0, node.balance_factor - 2)
        # node.balance_factor = node.balance_factor + self.height(
        #     new_node.right) - self.height(new_node)
        node.balance_factor = node.balance_factor + new_r_height - new_height
        new_node.balance_factor = new_node.balance_factor - 1 + min(
            0, node.balance_factor)

    def rotate_right(self, node):
        new_node = node.right
        new_height = self.height(new_node)
        new_l_height = self.height(new_node.left)
        node.right.parent = node.parent
        if self.root == node:
            self.root = node.right
        else:
            if node.is_right_child():
                node.parent.right = node.right
            else:
                node.parent.left = node.right
        if node.has_left_child():
            node.parent = node.right
            tmp_node = node.right.left
            node.right.left = node
            node.right = tmp_node
        else:
            node.parent = node.right
            node.right.left = node
            node.right = None
        # new_node.balance_factor += 1
        # node.balance_factor = min(0, node.balance_factor + 2)
        # node.balance_factor = node.balance_factor + self.height(
        #     new_node) - self.height(new_node.left)
        node.balance_factor = node.balance_factor + new_height - new_l_height
        new_node.balance_factor = new_node.balance_factor + 1 + max(
            0, node.balance_factor)

    def delete(self, value):
        pass

    def traverse(self, node, seq):
        if node is not None:
            self.traverse(node.left, seq)
            seq.append((node.data, node.balance_factor))
            self.traverse(node.right, seq)

    def __len__(self, ):
        return self.size

    def __repr__(self, ):
        seq = []
        self.traverse(self.root, seq)
        return ','.join(map(str, seq))
