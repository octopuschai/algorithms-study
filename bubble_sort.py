""" bubble sort """


def bubble_sort(seq):
    for times in range(len(seq) - 1, 0, -1):
        for i in range(times):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]


def short_bubble_sort(seq):
    """
    优化冒泡排序
    当遍历时，如果相邻数据没有冒泡交换过，则证明子序列已排序
    """
    for times in range(len(seq) - 1, 0, -1):
        exchange = 0
        for i in range(times):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                exchange = 1
        if not exchange:
            break
