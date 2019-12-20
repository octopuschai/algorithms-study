""" 动态规划 dynamic programming """


def make_change(coin_value_lists, change):
    """ 使用动态规划解决找零钱问题 """
    sloves = [0 for _ in range(change + 1)]  # 找零钱币数量最少表
    coin_used = [0 for _ in range(change + 1)]  # 记录找零钱币面值表，和slove表对应
    i = 1
    while i <= change:
        sloves[i] = change  # 保证初始值大于等于最少值
        for coin_value in coin_value_lists:  # 扫描零钱币面值表
            if i >= coin_value:
                min_coins = 1 + sloves[i - coin_value]
                # print(f'change({i}) {coin_value} {min_coins}')
                if sloves[i] > min_coins:
                    sloves[i] = min_coins  # 取最少值
                    coin_used[i] = coin_value  # 记录面值
        # print(sloves, coin_used)
        i += 1

    coins_detail = {}  # 最少零钱具体面值和相应数量
    index = change
    while index > 0:
        coin_value = coin_used[index]
        if coins_detail.get(coin_value):  # 是否有这个面值
            coins_detail[coin_value] += 1  # 有，计数加一
        else:
            coins_detail[coin_value] = 1  # 没有，增加这个面值并计数为一
        index = index - coin_value

    return sloves[change], coins_detail


if __name__ == "__main__":
    coin_value_lists = [1, 5, 7, 10, 21, 25]
    change = 63
    min_coins, coins_detail = make_change(coin_value_lists, change)
    print(f'coin_value_lists:', coin_value_lists)
    print(f'change({change}) min_coins={min_coins}')
    for k, v in coins_detail.items():
        print(f'coin_value:{k}, amount:{v}')
