""" binary tree """

from collections import deque


class BinaryTree(object):
    def __init__(self, data=None):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def insert_left(self, data=None):
        node = BinaryTree(data)
        if self.left is None:
            self.left = node
            node.parent = self
        else:
            node.left = self.left
            self.left = node
            node.parent = self

    def insert_right(self, data=None):
        node = BinaryTree(data)
        if self.right is None:
            self.right = node
            node.parent = self
        else:
            node.right = self.right
            self.right = node
            node.parent = self

    def get_data(self, ):
        return self.data

    def set_data(self, data):
        self.data = data

    def traverse(self, ):
        """ BFS tree node traverse """
        layer_num = 1
        tree_layers = deque()
        tree_layers.append(self)
        while tree_layers:
            layers = tree_layers.copy()
            tree_layers = deque()
            msg = f'layer({layer_num}): '
            while layers:
                parent_node = layers.popleft()
                msg += f'{parent_node.data}, '
                # print(f'{parent_node.data}')
                if parent_node.left is not None:
                    tree_layers.append(parent_node.left)
                if parent_node.right is not None:
                    tree_layers.append(parent_node.right)
            print(msg)
            layer_num += 1


def num2char(expression):
    res = []
    num = []
    for char in expression:
        if char in '0123456789':
            num.append(char)
        else:
            if num:
                res.append(''.join(num))
                num.clear()
            res.append(char)
    return res


def build_parse_tree(expression):
    operator_symbol = '+-/*'
    tree = BinaryTree()
    locate = tree
    exp_list = num2char(expression)
    for char in exp_list:
        if char == '(':
            locate.insert_left()
            locate = locate.left
        elif char == ')':
            locate = locate.parent
        elif char in operator_symbol:
            locate.set_data(char)
            locate.insert_right()
            locate = locate.right
        else:
            locate.set_data(char)
            locate = locate.parent
    return tree


def evaluate(parse_tree):
    if parse_tree.left is None and parse_tree.right is None:
        return int(parse_tree.data)
    if parse_tree.get_data() == '+':
        res = evaluate(parse_tree.left) + evaluate(parse_tree.right)
    elif parse_tree.get_data() == '-':
        res = evaluate(parse_tree.left) - evaluate(parse_tree.right)
    elif parse_tree.get_data() == '*':
        res = evaluate(parse_tree.left) * evaluate(parse_tree.right)
    elif parse_tree.get_data() == '/':
        res = evaluate(parse_tree.left) / evaluate(parse_tree.right)
    return res


if __name__ == "__main__":
    expressions = [
        '(3+(4*5))',
        '((100*11)/50)',
        '((10+33)*(593-274))',
    ]
    for expression in expressions:
        pt = build_parse_tree(expression)
        # pt.traverse()
        print(f'{expression}={evaluate(pt)}')
