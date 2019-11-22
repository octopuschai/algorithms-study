def find_min(seq) -> (int, 'item'):
    idx, min_item = 0, seq[0]
    for i, item in enumerate(seq[1:], 1):
        if item < min_item:
            idx, min_item = i, item
    return idx, min_item


def selection_sort(seq) -> list:
    new_seq = []
    seq = list(seq)
    while seq:
        idx, min_item = find_min(seq)
        del seq[idx]
        new_seq.append(min_item)
    return new_seq
