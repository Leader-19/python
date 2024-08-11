#todo list with oop

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.isComplete = False

    def complete(self):
        self.isCompplete = True

class Tasklist:
    def __init__(self):
        self.tasks = []

    def  add_task(self, task):
        self.tasks.append(task)
    
    def remove_task(self, task):
        self.tasks.remove(task)

    def get_all_task(self):
        return self.tasks
    
    def get_complete_task(self):
        completed_task = []
        for task in self.tasks:
            if task.isComplete:
                completed_task.append(task)
        return completed_task
    

go_to_school = Task("Go to school", "I will go to school")
washing_dic = Task("Go to washing dic", "I will go to washing dic")
go_out_side = Task("Go out side", "I will go out side")

task_list = Tasklist()

task_list.add_task(go_to_school)
task_list.add_task(washing_dic)
task_list.add_task(go_out_side)

go_out_side.complete()

# task_list.remove_task(go_out_side)
tasks = task_list.get_all_task()
for task in tasks:
    print(task.title)
    print(task.description)
    print(task.isComplete)
    print("=====>")