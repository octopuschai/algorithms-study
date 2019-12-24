""" hash search """


class HashTable(object):
    def __init__(self, ):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def get(self, key):
        idx = self.hash_algo(key)
        if self.slots[idx] is None:
            raise KeyError(f'key ({key}) not in Hash Table')
        elif self.slots[idx] == key:
            data = self.data[idx]
        else:
            idx = self.next_slot(idx)
            while self.slots[idx] is not None:
                if self.slots[idx] == key:
                    data = self.data[idx]
                    break
                idx = self.next_slot(idx)
            else:
                raise KeyError(f'key ({key}) not in Hash Table')
        return data

    def put(self, key, value):
        idx = self.hash_algo(key)
        if self.slots[idx] is None:
            self.slots[idx] = key
            self.data[idx] = value
        elif self.slots[idx] == key:
            self.data[idx] = value
        else:
            idx = self.next_slot(idx)
            while self.slots[idx] is not None and self.slots[idx] != key:
                idx = self.next_slot(idx)
            if self.slots[idx] is None:
                self.slots[idx] = key
                self.data[idx] = value
            else:
                self.data[idx] = value

    def next_slot(self, idx):
        """ obtain next available slots when collision """
        return (idx + 1) % self.size

    def hash_algo(self, key):
        """ hash algorithms """
        return key % self.size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __del__(self, key):
        pass

    def __repr__(self, ):
        msg = ''
        for i in range(self.size):
            if self.slots[i] is not None:
                msg += f'{self.slots[i]}: {self.data[i]}, '
        return '{' + msg + '}'
