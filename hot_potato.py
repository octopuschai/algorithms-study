from my_queue import MyQueue


def hot_potato(namelist, num):
    circle = MyQueue()
    for name in namelist:
        circle.add(name)
    while len(circle) != 1:
        for i in range(num):
            circle.add(circle.pop())
        circle.pop()
    return circle.pop()


if __name__ == "__main__":
    namelist = [
        'Iron man',
        'Hulk',
        'Thor',
        'Captain America',
        'Black Widow',
        'Hawk Eye',
    ]
    print(hot_potato(namelist, 7))
