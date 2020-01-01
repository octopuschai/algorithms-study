""" binary heap """


class BinaryHeap(object):
    def __init__(self, ):
        self.heap_list = [0]
        self.size = 0

    def insert(self, value):
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

    def del_min(self, ):
        if self.size == 0:
            raise IndexError('Error, Binary Heap is empty!')
        else:
            res = self.heap_list[1]
            tmp_list = self.heap_list[2:]
            self.__init__()
            for value in tmp_list:
                self.insert(value)
        return res
