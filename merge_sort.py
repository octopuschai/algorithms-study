""" merge sort """


def merge_sort(seq):
    mid = len(seq) // 2

    if mid < 1:
        return seq
    else:
        first_part = seq[:mid]
        second_part = seq[mid:]

        merge_sort(first_part)
        merge_sort(second_part)

        # 把已排序的first_part和second_part合并成整体排序
        # 分别比较后取两部分中最小值逐个加入原序列
        i = x = y = 0
        while x < len(first_part) and y < len(second_part):
            if first_part[x] <= second_part[y]:
                seq[i] = first_part[x]
                x += 1
                i += 1
            else:
                seq[i] = second_part[y]
                y += 1
                i += 1
        while x < len(first_part):
            seq[i] = first_part[x]
            x += 1
            i += 1
        while y < len(second_part):
            seq[i] = second_part[y]
            y += 1
            i += 1
