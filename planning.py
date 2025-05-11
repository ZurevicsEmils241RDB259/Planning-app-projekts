from datetime import datetime
import heapq

class Task:
    def __init__(self, name, priority, deadline, duration, category):
        self.name = name
        self.priority = priority
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")
        self.duration = duration
        self.category = category

    def need_to_do(self):
        return (self.deadline - datetime.now()).days < 2


class TaskPlanner:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        heapq.heappush(self.tasks, task)
        print(f"Added : {task}")
        
    def next_task(self):
        if self.tasks:
            return heapq.heappop(self.tasks)
        return None
    
    def show_tasks(self):
        if not self.tasks:
            print("No tasks planned")
            return
        
        print("All tasks in order of completion: ")
        sorted_tasks = sorted(self.tasks)
        for task in sorted_tasks:
            print(f" - {task}")

    def heapify_(self):
        heapq.heapify(self.tasks)
def get_task_from_user():
    print("\nEnter task details:")
    name = input("Task name: ")
    
    while True:
        try:
            priority = int(input("Priority (1=High, 2=Medium, 3=Low): "))
            if priority in {1, 2, 3}:
                break
            print("Please enter 1, 2, or 3")
        except ValueError:
            print("Please enter a number")

    while True:
        deadline = input("Deadline (YYYY-MM-DD): ")
        try:
            datetime.strptime(deadline, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD")

    while True:
        try:
            duration = int(input("Duration (minutes): "))
            break
        except ValueError:
            print("Please enter a number")

    return Task(name, priority, deadline, duration)
            
def main():
    scheduler = TaskPlanner()
    
    while True:
        print("\n=== Task Scheduler ===")
        print("1. Add a new task")
        print("2. Get next task to complete")
        print("3. View all tasks")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            task = get_task_from_user()
            scheduler.add_task(task)
            
        elif choice == "2":
            scheduler.get_next_task()
            
        elif choice == "3":
            scheduler.show_all_tasks()
            
        elif choice == "4":
            print("\nGoodbye!")
            break
            
        else:
            print("\nInvalid choice. Please enter 1-4")

if __name__ == "__main__":
    main()