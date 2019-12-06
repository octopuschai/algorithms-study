"""
https://facert.gitbooks.io/python-data-structure-cn/
3.9.2 中缀转后缀通用法:

假设中缀表达式是一个由空格分隔的标记字符串。 操作符标记是*，/，+和 - ，以及左右括号。
操作数是单字符 A，B，C 等。 以下步骤将后缀顺序生成一个字符串。
1.创建一个名为 opstack 的空栈以保存运算符。给输出创建一个空列表。
2.通过使用字符串方法拆分将输入的中缀字符串转换为标记列表。
3.从左到右扫描标记列表。
    - 如果标记是操作数，将其附加到输出列表的末尾。
    - 如果标记是左括号，将其压到 opstack 上。
    - 如果标记是右括号，则弹出 opstack，直到删除相应的左括号。将每个运算符附加到输出列表的末尾。
    - 如果标记是运算符，*，/，+或 - ，将其压入 opstack。但是，首先删除已经在 opstack 中具有更高
      或相等优先级的任何运算符，并将它们加到输出列表中。
4.当输入表达式被完全处理时，检查 opstack。仍然在栈上的任何运算符都可以删除并加到输出列表的末尾。
"""

# operator_symbol = ['+', '-', '*', '/', '(', ')']
operator_symbol = '+-*/()'

numbers = '1234567890'


def infix_to_postfix(expression: str) -> str:
    """ 中缀表达式转换成后缀表达式 """
    op_stack = []
    output = []
    for char in expression:
        # print(f'char:{char!r}, op_stack:{op_stack}, output:{output}')
        if char in operator_symbol:
            if char == '(':
                op_stack.append(char)
            elif char == ')':
                while True:
                    flag = op_stack.pop()
                    if flag == '(':
                        break
                    output.append(flag)
            else:
                if op_stack and op_stack[-1] in operator_symbol[:-2]:
                    char_priority = int(operator_symbol.index(char) / 2)
                    top_priority = int(operator_symbol.index(op_stack[-1]) / 2)
                    if top_priority >= char_priority:
                        output.append(op_stack.pop())
                op_stack.append(char)
        else:
            output.append(char)

    while op_stack:
        output.append(op_stack.pop())

    return ''.join(output)


def str_to_int(string) -> int:
    return sum([
        int(string[n]) * 10**(len(string) - n - 1) for n in range(len(string))
    ])


def do_math(op: str, num1: int, num2: int) -> int:
    if op == '+':
        res = num1 + num2
    elif op == '-':
        res = num1 - num2
    elif op == '*':
        res = num1 * num2
    else:
        res = num1 / num2
    return res


def postfix_to_value(expression: str) -> int:
    """ 后缀表达式求值 """
    stack = []
    for char in expression:
        if char in numbers:
            stack.append(int(char))
        elif char in operator_symbol[:-2]:
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(do_math(char, num1, num2))
        else:
            raise ValueError('Invalid Postfix expression!')
    return stack.pop()


if __name__ == "__main__":
    infix_exps = [
        '(A+B)*C',
        'A*B+C*D',
        '(A+B)*C-(D-E)*(F+G)',
        '((A+B)*C-D)/(E-F*(G+H))',
    ]

    for infix_exp in infix_exps:
        postfix_exp = infix_to_postfix(infix_exp)
        print(f'Infix: {infix_exp} ==> Postfix: {postfix_exp}')

    infix_exp = '(7+8)/(3+2)'
    postfix_exp = infix_to_postfix(infix_exp)
    value = postfix_to_value(postfix_exp)
    print(f'Infix: {infix_exp} ==> Postfix: {postfix_exp} , value = {value}')
