from sortedcontainers import SortedList
from datetime import datetime

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.status = False

    def mark_complete(self):
        self.status = True

class TaskList:
    def __init__(self):
        self.tasks = SortedList(key=lambda task: task.due_date)

    def add_task(self, description, due_date):
        try:
            self.tasks.add(Task(description, datetime.strptime(due_date, '%d.%m.%y')))
            return True
        except ValueError:
            print('Invalid due date. Please try again.')
            return False

    def show_pending_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            if not task.status:
                print(f'{i}. {task.description} - {task.due_date.strftime("%d.%m.%y")}')
        print()

    def mark_task_complete(self, index):
        i = 1
        for task in self.tasks:
            if task.status:
                continue
            if i == index:
                task.mark_complete()
                break
            i += 1

task_list = TaskList()
while True:
    print('1. Add task')
    print('2. Show pending tasks')
    print('3. Mark task complete')
    print('4. Exit')
    choice = input('Enter your choice: ')
    print()

    if choice == '1':
        description = input('Enter task description: ')
        correct_date = False
        while not correct_date:
            due_date = input('Enter due date (dd.mm.yy): ')
            correct_date = task_list.add_task(description, due_date)
    elif choice == '2':
        task_list.show_pending_tasks()
    elif choice == '3':
        index = int(input('Enter task index to mark as complete: '))
        task_list.mark_task_complete(index)
    elif choice == '4':
        break
    else:
        print('Invalid choice. Please try again.')