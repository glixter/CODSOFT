import sys


class ToDoList:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "status": "Incomplete"})
        print(f"Added task: '{task}'")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found!")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = task["status"]
                print(f"{idx}. {task['task']} - {status}")

    def update_task(self, task_number, new_task):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["task"] = new_task
            print(f"Task {task_number} updated to: '{new_task}'")
        else:
            print(f"Task {task_number} does not exist!")

    def mark_task_complete(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["status"] = "Complete"
            print(f"Task {task_number} marked as complete")
        else:
            print(f"Task {task_number} does not exist!")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Removed task: '{removed_task['task']}'")
        else:
            print(f"Task {task_number} does not exist!")


if __name__ == "__main__":
    todo_list = ToDoList()

    todo_list.add_task("Buy groceries")
    todo_list.add_task("Write Python script")

    todo_list.list_tasks()

    todo_list.update_task(1, "Buy groceries and fruits")

    todo_list.mark_task_complete(2)

    todo_list.list_tasks()

    todo_list.delete_task(1)

    todo_list.list_tasks()
