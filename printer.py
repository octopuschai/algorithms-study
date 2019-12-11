import random

from my_queue import MyQueue


class Task(object):
    """ 打印任务 """
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self, ):
        return self.timestamp

    def getPages(self, ):
        return self.pages

    def waitTime(self, current_time):
        return current_time - self.timestamp


class Printer(object):
    """ 打印机 """
    def __init__(self, pages_per_minute):
        self.pagerate = pages_per_minute
        self.task = None
        self.time_remain = 0

    def tick(self, ):
        """ 执行打印任务，递减时间 """
        if self.task:
            self.time_remain -= 1
            if self.time_remain <= 0:
                self.task = None

    def isBusy(self, ):
        if self.task:
            return True
        else:
            return False

    def startTask(self, new_task):
        """ 开始打印任务，根据每分钟打印页数计算任务花费时间 """
        self.task = new_task
        self.time_remain = new_task.getPages() * 60 / self.pagerate


def new_task():
    """ 新任务生成器，每三分钟（180秒）生成一个任务 """
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


def simulation(total_seconds, pages_per_pages):
    """ 模拟运行环境 """
    printer = Printer(pages_per_pages)
    printer_queue = MyQueue()
    time_per_task = []
    for current_second in range(total_seconds):
        if new_task():
            printer_queue.add(Task(current_second))
        if (len(printer_queue) != 0) and (not printer.isBusy()):
            current_task = printer_queue.pop()
            printer.startTask(current_task)
            time_per_task.append(current_task.waitTime(current_second))
        printer.tick()
    avg_time_per_task = sum(time_per_task) / len(time_per_task)
    print(
        'Average time {:6.2f} secs, total {} tasks, {} tasks remaining'.format(
            avg_time_per_task,
            len(time_per_task),
            len(printer_queue),
        ))


if __name__ == "__main__":
    for i in range(10):
        simulation(3600, 5)
    print('='*80)
    for i in range(10):
        simulation(3600, 10)
