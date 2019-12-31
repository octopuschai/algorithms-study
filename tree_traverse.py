from binary_tree import build_parse_tree


def pre_order(tree):
    """ 树的前序遍历 """
    if tree:
        print(tree.get_data(), end='')
        pre_order(tree.left)
        pre_order(tree.right)


def mid_order(tree):
    """ 树的中序遍历 """
    if tree:
        mid_order(tree.left)
        print(tree.get_data(), end='')
        mid_order(tree.right)


def post_order(tree):
    """ 树的后序遍历 """
    if tree:
        post_order(tree.left)
        post_order(tree.right)
        print(tree.get_data(), end='')


if __name__ == "__main__":
    expression = '(3+(4*5))'
    pt = build_parse_tree(expression)
    print('\ntree pre_order: ')
    pre_order(pt)
    print('\ntree mid_order: ')
    mid_order(pt)
    print('\ntree post_order: ')
    post_order(pt)
