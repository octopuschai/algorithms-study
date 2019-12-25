""" shell sort """


def gap_insert_sort(seq, start=0, gap=1):
    for i in range(start + gap, len(seq), gap):
        value = seq[i]
        p = i
        while seq[p - gap] > value and p >= gap:
            seq[p] = seq[p - gap]
            p -= gap
        seq[p] = value


def shell_sort(seq):
    gap = len(seq) // 2
    while gap > 0:
        for i in range(gap):
            gap_insert_sort(seq, i, gap)
        gap //= 2
