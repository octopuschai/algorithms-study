""" 汉诺塔问题 Hanoi"""

steps = []  # 记录整个移动步骤


def hanoi(nums, start_pole, mid_pole, end_pole):
    """
    使用递归解决汉诺塔问题

    思路：
    考虑n个盘要完成移动，只要情况是中间柱有n-1个盘，起始柱有第n号盘，就可以容易解决
    1、移动第n号盘从起始柱到最终柱
    2、解决n-1个盘从中间柱移动到最终柱，此时起始柱作为临时中间柱使用
    3、然后要完成以上情况，需要首先完成把n-1个盘从起始柱移动到中间柱
    4、实际就是考虑n-1个盘完成移动，此时最终柱作为临时中间柱使用
    以此类推，直到考虑1个盘完成移动，只要从起始柱直接一次移动到最终柱就可以了

    因此分解整个移动过程成三个步骤：
    第一步：完成n-1个盘从起始柱移动到中间柱
    第二步：从起始柱移动第n号盘到最终柱
    第三步：完成n-1个盘从中间柱移动到最终柱
    限制条件：当n=1个盘，直接从起始柱移动到最终柱
    """
    if nums == 1:
        # 限定条件，当1个盘时，只有一个步骤，只要移动一次
        step = f'(No.{nums}) dish, {start_pole} -> {end_pole}'
        steps.append(step)
        times = 1
    else:
        # 步骤1，将n-1个盘，从起始柱移到中间柱，此时最终柱作为临时中间柱
        time1 = hanoi(nums - 1, start_pole, end_pole, mid_pole)

        # 步骤2，将n号盘从起始柱移到终点柱，只要移动一次
        step = f'(No.{nums}) dish, {start_pole} -> {end_pole}'
        steps.append(step)

        # 步骤3，将n-1个盘，从中间柱移到最终柱，此时起始柱作为临时中间柱
        time2 = hanoi(nums - 1, mid_pole, start_pole, end_pole)

        # 总移动次数times
        times = time1 + time2 + 1
    return times


if __name__ == "__main__":
    nums = 4
    times = hanoi(nums, 'A', 'B', 'C')
    print(f'Hanoi, {nums} dishes, times={times}')
    for index, step in enumerate(steps, 1):
        print(f'step {index:<2d} : {step}')
