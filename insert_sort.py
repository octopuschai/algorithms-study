""" insert sort """


def insert_sort(seq):
    """ insert sorted self """
    for i in range(1, len(seq)):
        value = seq[i]
        p = i  # p is a position variable of insert
        while seq[p - 1] > value and p > 0:
            seq[p] = seq[p - 1]
            p -= 1
        seq[p] = value


def insert_sort2(seq):
    """ return a new insert sorted seq """
    new_seq = [seq[0]]
    for i in range(1, len(seq)):
        for j in range(len(new_seq) - 1, -1, -1):
            if seq[i] >= new_seq[j]:
                new_seq.insert(j + 1, seq[i])
                break
        else:
            new_seq.insert(0, seq[i])
    return new_seq
