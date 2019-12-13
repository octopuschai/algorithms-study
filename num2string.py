from my_queue import MyDeque

stack = MyDeque()


def num2string(num, base=10):
    convertString = '0123456789ABCDEF'
    while num:
        if num // base == 0:
            stack.add(convertString[num])
        else:
            stack.add(convertString[num % base])
        num //= base
    res = ''
    while stack:
        res = res + stack.pop()
    return res


if __name__ == "__main__":
    print(num2string(768))
