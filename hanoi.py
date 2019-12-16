""" 汉诺塔问题 Hanoi"""

steps = []  # 记录整个移动步骤


def hanoi(num, start_pole, mid_pole, end_pole):
    """
    使用递归解决汉诺塔问题
    思路：
    考虑n个盘要完成移动，只要情况是中间柱有n-1个盘，起始柱有第n号盘
    1、移动第n号盘从起始柱到最终柱
    2、递归解决n-1个盘从中间柱移动到最终柱
    分解整个移动过程
    1、
    """
    if num == 1:
        # 限定条件，当1个盘时，只有一个步骤，只要移动一次
        step = f'({num}) dish, {start_pole} -> {end_pole}'
        steps.append(step)
        times = 1
    else:
        # 步骤1，将n-1个盘，从起始柱移到中间柱，此时最终柱做为临时中间柱
        time1 = hanoi(num - 1, start_pole, end_pole, mid_pole)
        # 步骤2，将n号盘从起始柱移到终点柱，只要移动一次
        step = f'({num}) dish, {start_pole} -> {end_pole}'
        steps.append(step)
        # 步骤3，将n-1个盘，从中间柱移到最终柱，此时起始柱做为临时中间柱
        time2 = hanoi(num - 1, mid_pole, start_pole, end_pole)
        # 总移动次数times
        times = time1 + time2 + 1
    return times


if __name__ == "__main__":
    nums = 4
    times = hanoi(nums, 'A', 'B', 'C')
    print(f'Hanoi, {nums} dishes, times={times}')
    for index, step in enumerate(steps, 1):
        print(f'step{index} : {step}')
