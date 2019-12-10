import random


class Task(object):
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)


class Printer(object):
    def __init__(self, ppm):
        self.pagerate = ppm
        self.task = None
        self.time_remain = 0

    def tick(self, ):
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
        self.task = new_task
        self.time_remain = new_task.getPages() * 60 / self.pagerate
