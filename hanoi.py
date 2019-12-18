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


hanoi_loop_steps = []  # 记录整个移动步骤


def hanoi_loop(nums):
    """
    非递归解决汉诺塔问题

    思路：
    用递归解汉诺塔，移动步骤中1号盘总是从起始柱、中间柱、最终柱逐一移动周而复始，形成一个环
    若A为起始柱、C为最终柱、B为中间柱
    当盘数为奇数时，环顺序为A,C,B
    当盘数为偶数时，环顺序为A,B,C
    当1号盘移到下一柱后，比较剩下两个柱的盘号，并按汉诺塔约束条件（只允许小号盘放在大号盘上）进行
    当剩下两个柱都为空柱时，说明已到达最终状态，完成移动
    """
    from collections import deque
    # 初始化a,b,c柱 每个柱子都LIFO，实际是栈结构，用list模拟
    a = [i for i in range(nums, 0, -1)]
    b, c = [], []

    # 柱子顺序列表，构成一个环，使用循环队列，用deque模拟
    if nums % 2:
        # 当奇数时，柱子初始顺序
        pole_order = deque([(a, 'A'), (c, 'C'), (b, 'B')], maxlen=3)
    else:
        # 当偶数时，柱子初始顺序
        pole_order = deque([(a, 'A'), (b, 'B'), (c, 'C')], maxlen=3)

    times = 0
    while True:
        # 柱子顺序作为循环队列使用，取当前柱号，并前进到下一柱
        curr_pole, curr_pole_name = pole_order.popleft()
        pole_order.append((curr_pole, curr_pole_name))

        # 下一柱号
        next_pole, next_pole_name = pole_order[0]

        # 从当前柱取1号盘放入下一柱
        dish_num = curr_pole.pop()
        next_pole.append(dish_num)

        # 记录步骤
        times += 1
        step = f'(No.{dish_num}) dish, {curr_pole_name} -> {next_pole_name}'
        hanoi_loop_steps.append(step)

        # 取剩余两个柱子柱号one,two
        one, one_name = pole_order[1]
        two, two_name = pole_order[2]
        if not bool(one) and not bool(two):
            # 剩余两个柱子为空，说明已经完成移动
            break
        elif not bool(one):
            # one柱子为空，取two柱子顶端盘子放入one柱子
            step = f'(No.{two[-1]}) dish, {two_name} -> {one_name}'
            hanoi_loop_steps.append(step)
            one.append(two.pop())
            times += 1
        elif not bool(two):
            # two柱子为空，取one柱子顶端盘子放入two柱子
            step = f'(No.{one[-1]}) dish, {one_name} -> {two_name}'
            hanoi_loop_steps.append(step)
            two.append(one.pop())
            times += 1
        elif one[-1] > two[-1]:
            # one柱子顶端盘号大于two柱子顶端盘号，取two柱子顶端盘子放入one柱子
            step = f'(No.{two[-1]}) dish, {two_name} -> {one_name}'
            hanoi_loop_steps.append(step)
            one.append(two.pop())
            times += 1
        else:
            # two柱子顶端盘号大于one柱子顶端盘号，取one柱子顶端盘子放入two柱子
            step = f'(No.{one[-1]}) dish, {one_name} -> {two_name}'
            hanoi_loop_steps.append(step)
            two.append(one.pop())
            times += 1
    return times


if __name__ == "__main__":
    nums = 4
    times = hanoi(nums, 'A', 'B', 'C')
    print(f'Hanoi, {nums} dishes, move times={times}')
    for index, step in enumerate(steps, 1):
        print(f'step {index:<2d} : {step}')

    print('=' * 80)
    times = hanoi_loop(nums)
    print(f'Hanoi_loop, {nums} dishes, move times={times}')
    for index, step in enumerate(hanoi_loop_steps, 1):
        print(f'step {index:<2d} : {step}')

    import time
    for nums in (5, 10, 15, 20):
        start = time.time()
        hanoi(nums, 'A', 'B', 'C')
        elapsed = time.time() - start

        start = time.time()
        hanoi_loop(nums)
        loop_elapsed = time.time() - start

        print('{} dishes, hanoi {:.5f}, hanoi_loop {:.5f}'.format(
            nums,
            elapsed,
            loop_elapsed,
        ))
