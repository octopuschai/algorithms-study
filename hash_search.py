class HashTable(object):
    def __init__(self, ):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def __getitem__(self, key):
        idx = self.hash_algo(key)
        if self.slots[idx] is None:
            raise ValueError(f'key ({key}) not in Hash Table')

    def __setitem__(self, key, value):
        idx = self.hash_algo(key)
        if self.slots[idx] is None:
            self.slots[idx] = key
            self.data[idx] = value
        else:
            idx = self.next_slot(idx)
            while self.slots[idx] is not None:
                idx = self.next_slot(idx)
            self.slots[idx] = key
            self.data[idx] = value

    def next_slot(self, idx):
        return (idx + 1) % 11

    def hash_algo(self, key):
        return key % 11
