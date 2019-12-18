from collections import deque
from pprint import pprint

track = deque(list('abcdefghijklmnopqrstuvwxyz'), maxlen=26)

maze_map = [
    ['+', '+', '+', ' ', '+', '+', '+', '+', '+', '+'],
    ['+', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '+'],
    ['+', ' ', '+', '+', '+', '+', '+', '+', ' ', '+'],
    ['+', ' ', ' ', ' ', ' ', '+', ' ', ' ', ' ', '+'],
    ['+', ' ', '+', '+', ' ', '+', '+', '+', '+', '+'],
    ['+', ' ', '+', ' ', ' ', ' ', ' ', ' ', '+', '+'],
    ['+', ' ', '+', ' ', '+', '+', '+', ' ', '+', '+'],
    ['+', '+', '+', ' ', '+', '+', ' ', ' ', ' ', '+'],
    ['+', '+', '+', '+', '+', '+', '+', '+', ' ', '+'],
    ['+', '+', '+', '+', '+', '+', '+', '+', 'E', '+'],
]


def search_maze(maze, start_x, start_y):
    """ 递归搜索迷宫 """
    pos = maze[start_x][start_y]
    if pos == 'E':  # exit
        return True
    elif pos == ' ':  # way
        maze[start_x][start_y] = track[0]  # make mark
        track.rotate(-1)
        ml = search_maze(maze, start_x, start_y - 1)  # move left
        if ml:
            return True
        mr = search_maze(maze, start_x, start_y + 1)  # move right
        if mr:
            return True
        mu = search_maze(maze, start_x - 1, start_y)  # move up
        if mu:
            return True
        md = search_maze(maze, start_x + 1, start_y)  # move down
        return md
    elif pos == '+':  # wall
        return False
    else:  # marked
        return False


if __name__ == "__main__":
    if search_maze(maze_map, 5, 4):
        pprint(maze_map)
    else:
        print("Sorry, Maze has no way out!")
