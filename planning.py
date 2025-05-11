from datetime import datetime
import heapq

class Task:
    def __init__(self, name, priority, deadline, duration, category):
        self.name = name
        self.priority = priority
        self.deadline = deadline
        self.duration = duration
        self.category = category

    def need_to_do(self):
        return (self.deadline - datetime.now()).days < 2


class TaskPlanner:
    def __init__(self, task):
        self.task_heap = []
        self.task_dict = {}

    def add_task(self, task):
        print()