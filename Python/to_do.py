def menu():
    print("to do by yasir")
    print("1 add task")
    print ("2 show task")
    print("3 delate task")  
    print ("4 quit")

def enter_task(tasks):
     task = input("enter task ")
     tasks.append(task)
     print("task added")


def show_tasks(tasks):
    if len(tasks) == 0:
        print("no task added")
    else:
        i = 0
        while i < len(tasks):
            print(f"{i+1}. {tasks[i]}")
            i += 1

def deleat_task(tasks):
    show_tasks(tasks)
    if len(tasks) == 0:
      return
    num = input("enter number of task to delete ")

    removed = tasks.pop(num - 1)
    print("deleted",removed)
 
def edit_task(tasks):
    show_tasks(tasks)
    if len(tasks) == 0:
      return
    editNum = input("enter number of task to edit ")

    editTask=input("enter task name")
    print (editNum)
    print(editTask)
    editNum = int(editNum)

    tasks[editNum - 1] = editTask

    
    
def main():
  tasks=[]
  while True:
        menu()
        choice = input("enter choice ")
        if choice == "1":
            enter_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            deleat_task(tasks)
        elif choice == "4":
            print("goodbye")
            break
        elif choice == "5":
            edit_task(tasks)
            print ("5")
        else:
            print("inviled choice,try again")

main()