Task =[]



def AddTask():
    n = int(input("Enter total number of task: "))
    for i in range(n):
        task = input("Add Task: ")
        Task.append(task)
    return Task



def ViewTask():
    print("Here is the Tasks: ")
    for n, elements in enumerate(Task, start=1):
        print(f"  {n}.{elements}  ")



def UpdateTask():
    while True:
        task = input("\nPlease enter a name of a task you want to update: ").lower()
        yes_or_no = input(f"\nAre you sure to update {task} from your Task Liast? (Y/N): ").lower()
        if yes_or_no =="y":
            update_task = input(f"Enter a Task you want to update {task} with :").lower()
            index = Task.index(task)
            Task[index] = update_task
            print("Your Task is updated in To Do List.")
            break
             
    

def Exit():
    return 0

   

while True:
    print('''
       1. Add Task
       2. Upadte Task
       3. View Task
       4. Exit
       ''')   
    choice = int(input('Enter your choice: '))
    opration =[AddTask,UpdateTask,ViewTask,Exit]
    output = opration[choice - 1]()
    if choice == 4:
        break
