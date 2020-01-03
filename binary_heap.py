""" binary heap """


class BinaryHeap(object):
    """ Binary Heap, top element (heap_list[1]) is an minimum element """
    def __init__(self, seq=None):
        self.heap_list = [0]
        self.size = 0
        if seq:
            self.build(seq)

    def insert(self, value):
        """ insert an element """
        self.heap_list.append(value)
        self.size += 1
        cur_idx = self.size
        par_idx = self.size // 2
        while par_idx > 0:
            if self.heap_list[cur_idx] <= self.heap_list[par_idx]:
                self.heap_list[par_idx], self.heap_list[
                    cur_idx] = self.heap_list[cur_idx], self.heap_list[par_idx]
            else:
                break
            cur_idx = par_idx
            par_idx = par_idx // 2

    def pop(self, ):
        """ pop the minimum element from Binary Heap """
        if self.size == 0:
            raise IndexError('Error, Binary Heap is empty!')
        else:
            res = self.heap_list[1]
            self.heap_list[1] = self.heap_list[self.size]
            self.heap_list.pop()
            self.size -= 1
            p = 1
            while True:
                n = self.min_child(p)
                if n is not None and (self.heap_list[p] > self.heap_list[n]):
                    self.heap_list[p], self.heap_list[n] = self.heap_list[
                        n], self.heap_list[p]
                    p = n
                else:
                    break
        return res

    def min_child(self, par_idx):
        """ compare left child and right child, return min child or None """
        left = par_idx * 2
        right = left + 1
        if left > self.size:
            return None
        elif left == self.size:
            return left
        else:
            if self.heap_list[left] < self.heap_list[right]:
                return left
            return right

    def build(self, seq):
        """ build a Binary Heap from a sequence """
        for item in seq:
            self.insert(item)
