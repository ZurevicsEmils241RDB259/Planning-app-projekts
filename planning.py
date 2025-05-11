from datetime import datetime
import heapq

class Task:
    def __init__(self, name, deadline, duration_hours):
        self.name = name
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")
        self.duration_hours = duration_hours
        self.priority = self.calculate_priority()

    def calculate_priority(self):
        time_left_days = (self.deadline - datetime.now()).total_seconds() / (60 * 60 * 24)
        urgency = time_left_days / self.duration_hours
        return urgency

    def __lt__(self, other):
        return self.priority < other.priority 
    
    def __str__(self):
        days_left = (self.deadline - datetime.now()).days
        return (f"{self.name} (Deadline: {self.deadline.date()}, "f"Duration: {self.duration_hours} hours, "f"Days left: {days_left}, "f"Priority: {self.priority:.2f})")

class TaskPlanner:
    def __init__(self):
        self.heap = []

    def add_task(self, task):
        heapq.heappush(self.heap, task)
        print(f"Added: {task}")
        
    def get_next_task(self):
        if self.heap:
            next_task = heapq.heappop(self.heap)
            print(f"Next task: {next_task}")
            return next_task
        else:
            print("No tasks.")
            return None
    
    def show_all_tasks(self):
        if not self.heap:
            print("No tasks planned")
            return
        
        print("\nAll tasks in order of priority:") 
        temp_heap = self.heap.copy()
        while temp_heap:
            task = heapq.heappop(temp_heap)
            print(f" - {task}")

def get_task_from_user():
    print("\nEnter task details:")
    name = input("Task name: ")
    
    while True:
        deadline = input("Deadline (YYYY-MM-DD): ")
        try:
            datetime.strptime(deadline, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD")

    while True:
        try:
            duration_hours = float(input("Duration (hours): "))
            if duration_hours <= 0:
                print("Duration must be positive")
                continue
            break
        except ValueError:
            print("Please enter a number")

    return Task(name, deadline, duration_hours)
            
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
            print("\n")
            task = get_task_from_user()
            scheduler.add_task(task)
            print("\n")
            
        elif choice == "2":
            print("\n")
            scheduler.get_next_task()
            print("\n")
            
        elif choice == "3":
            print("\n")
            scheduler.show_all_tasks()
            print("\n")
            
        elif choice == "4":
            print("\nGoodbye!")
            break
            
        else:
            print("\nInvalid choice. Please enter 1-4")

if __name__ == "__main__":
    main()