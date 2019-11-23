def quick_sort(seq) -> list:
    if len(seq) <= 1:
        return seq
    pivot = seq[0]
    # l_sub = [i for i in seq[1:] if i <= pivot]
    # g_sub = [i for i in seq[1:] if i > pivot]
    l_sub, g_sub = [], []
    for item in seq[1:]:
        if item > pivot:
            g_sub.append(item)
        else:
            l_sub.append(item)
    return quick_sort(l_sub) + [pivot] + quick_sort(g_sub)


def quick_sort2(seq) -> list:
    long = len(seq)
    if long <= 1:
        return seq
    pivot = seq.pop(int(long / 2))
    l_sub, g_sub = [], []
    for item in seq:
        if item > pivot:
            g_sub.append(item)
        else:
            l_sub.append(item)
    return quick_sort(l_sub) + [pivot] + quick_sort(g_sub)
