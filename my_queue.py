class LinkNode(object):
    """ 模拟单向链表 """
    def __init__(self, value=None, next_=None):
        self._value = value
        self._next = next_


class MyQueue:
    """ 模拟队列 """
    def __init__(self, ):
        self.head = None
        self.tail = None

    def __len__(self, ):
        count = 0
        head = self.head
        while head is not None:
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
            raise IndexError('Error: Queue is empty!')
        res = self.head._value
        if self.tail._next is None:
            self.head = self.tail = None
        else:
            self.head = self.head._next
        return res


class DoubleLinkNode(object):
    """ 模拟双向链表 """
    def __init__(self, value=None, prev=None, next_=None):
        self._value = value
        self._prev = prev
        self._next = next_


class MyDeque:
    """ 模拟双向队列 """
    def __init__(self, ):
        self.head = None
        self.tail = None

    def __len__(self, ):
        count = 0
        head = self.head
        while head is not None:
            head = head._next
            count += 1
        return count

    def __repr__(self, ):
        elements = []
        head = self.head
        while head is not None:
            elements.append(head._value)
            head = head._next
        return repr(elements)

    def add(self, value):
        new_node = DoubleLinkNode(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node._prev = self.tail
            self.tail._next = new_node
            self.tail = new_node

    def addleft(self, value):
        new_node = DoubleLinkNode(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node._next = self.head
            self.head._prev = new_node
            self.head = new_node

    def pop(self, ):
        if len(self) == 0:
            raise IndexError('Error: Deque is empty!')
        res = self.tail._value
        if self.tail._prev is None:
            self.head = self.tail = None
        else:
            self.tail = self.tail._prev
            self.tail._next = None
        return res

    def popleft(self, ):
        if len(self) == 0:
            raise IndexError('Error: Deque is empty!')
        res = self.head._value
        if self.head._next is None:
            self.head = self.tail = None
        else:
            self.head = self.head._next
            self.head._prev = None
        return res

    def clear(self, ):
        while self.head is not None:
            self.popleft()

    def index(self, value):
        pos = 0
        head = self.head
        if len(self) == 0:
            raise IndexError('Error: Deque is empty!')
        while head is not None:
            if head._value == value:
                return pos
            head = head._next
            pos += 1
        else:
            raise ValueError(f"Error: Deque has't this element {value!r}!")

    def insert(self, pos, value):
        size = len(self)
        if pos < 0:
            raise IndexError("Error: position can't be negtive!")
        elif pos == 0:
            self.addleft(value)
        elif pos >= size:
            self.add(value)
        else:
            count = 0
            point = self.head
            new_node = DoubleLinkNode(value)
            while count < pos:
                point = point._next
                count += 1
            p, n = point._prev, point
            p._next = new_node
            new_node._prev = p
            n._prev = new_node
            new_node._next = n

    def remove(self, value):
        head = self.head
        if len(self) == 0:
            raise IndexError('Error: Deque is empty!')
        while head is not None:
            if head._value == value:
                p = head._prev
                n = head._next
                if p is None:
                    self.head = n
                else:
                    p._next = n
                if n is None:
                    self.tail = p
                else:
                    n._prev = p
                break
            head = head._next
        else:
            raise ValueError(f"Error: Deque has't this element {value!r}!")

    def sort(self, reverse=False):
        elements = []
        head = self.head
        while head is not None:
            elements.append(head._value)
            head = head._next
        elements.sort(reverse=reverse)
        self.clear()
        for element in elements:
            self.add(element)
