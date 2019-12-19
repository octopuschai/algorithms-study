""" 动态规划 dynamic programming """


def make_change(coin_value_lists, change):
    """ 使用动态规划解决找零钱问题 """
    sloves = [0 for _ in range(change + 1)]  # 找零钱最优解表
    i = 1
    while i <= change:
        sloves[i] = change  # 保证初始值大于等于最优解
        for coin_value in coin_value_lists:  # 扫描钱币面值表
            if i >= coin_value:
                min_coins = 1 + sloves[i - coin_value]
                # print(f'change({i}) {coin_value} {min_coins}')
                if sloves[i] > min_coins:
                    sloves[i] = min_coins  # 取最优解
        i += 1
    return sloves[change]


if __name__ == "__main__":
    coin_value_lists = [1, 5, 7, 10, 21, 25]
    change = 63
    min_coins = make_change(coin_value_lists, change)
    print(f'coin_value_lists:', coin_value_lists)
    print(f'change({change}) min_coins={min_coins}')
