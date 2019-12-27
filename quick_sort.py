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
    pivot = seq.pop(long // 2)
    l_sub, g_sub = [], []
    for item in seq:
        if item > pivot:
            g_sub.append(item)
        else:
            l_sub.append(item)
    return quick_sort2(l_sub) + [pivot] + quick_sort2(g_sub)


def quick_sort3(seq):
    """ quick sorted self """
    q_sort(seq, 0, len(seq) - 1)


def q_sort(seq, left_pos, right_pos):
    left, right = left_pos, right_pos
    if left >= right:
        return
    pivot = seq[left]
    left += 1
    while True:
        while seq[left] < pivot and left <= right:
            left += 1
        while seq[right] > pivot and left <= right:
            right -= 1
        if left < right:
            seq[left], seq[right] = seq[right], seq[left]
        else:
            break

    # seq[left_pos](pivot),seq[right] exchange their value
    seq[left_pos], seq[right] = seq[right], seq[left_pos]
    # now seq[right]=pivot

    # print(f'right:seq[{right}]={seq[right]}', seq)
    q_sort(seq, left_pos, right - 1)
    q_sort(seq, right + 1, right_pos)
