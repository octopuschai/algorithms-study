""" binary tree """

from collections import deque


class BinaryTree(object):
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert_left(self, node):
        if self.left is None:
            self.left = node
        else:
            node.left = self.left
            self.left = node

    def insert_right(self, node):
        if self.right is None:
            self.right = node
        else:
            node.right = self.right
            self.right = node

    def get_data(self, ):
        return self.data

    def set_data(self, data):
        self.data = data

    def traverse(self, ):
        tree = []
        tree_layers = deque()
        tree_layers.append(self)
        while deque:
            parent_node = deque.popleft()
            print(f'{parent_node.data}')
            if parent_node.left is not None:
                tree_layers.append(parent_node.left)
            elif parent_node.right is not None:
                tree_layers.append(parent_node.right)
