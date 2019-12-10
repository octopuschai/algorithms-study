class LinkNode(object):
    """ 模拟单链表 """
    def __init__(self, value=None, next_=None):
        self._value = value
        self._next = next_


class MyQueue:
    """ 模拟队列 """
    def __init__(self, ):
        self.head = None
        self.tail = None

    def __len__(self, ):
        if self.head is None:
            return 0
        count = 1
        head, tail = self.head, self.tail
        while head != tail:
            head = head._next
            count += 1
        return count

    def add(self, value):
        new_node = LinkNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail._next = new_node
            self.tail = new_node

    def pop(self, ):
        if len(self) == 0:
            raise ValueError('Error Queue is empty!')
        res = self.head._value
        self.head = self.head._next
        return res
