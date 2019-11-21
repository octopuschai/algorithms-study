def binary_search(seq, item) -> bool:
    low, high = 0, len(seq)
    if high == 0:
        raise ValueError('Original Seq is empty!')
    seq = sorted(seq)
    while low < high:
        idx = int((low + high) / 2)
        if seq[idx] < item:
            low = idx + 1
        elif seq[idx] > item:
            high = idx
        else:
            return True
    return False
