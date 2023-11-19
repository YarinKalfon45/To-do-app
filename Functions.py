from datetime import datetime


def showtime():
    now = datetime.now()
    date_str = now.strftime("%d/%m/%Y")
    time_str = now.strftime('%H:%M:%S')
    print(f"Today is {date_str}, The current time is {time_str}")
    return now


def get_lst(filepath):
    with open(filepath, "r") as file:
        lst = file.readlines()
        return lst


def show_list(filepath):
    print("Your tasks for today are:")
    lst = get_lst(filepath)
    for i in range(len(lst)):
        print(f"{i + 1}.{lst[i]}")
    print("\n", end='')


def add_task(filepath, task):
    with open(filepath, "a") as file:
        file.write(task.capitalize() + '\n')


def edit_task(filepath,old_task,new_task):
    lst = []
    lst = get_lst(filepath)
    index = lst.index(old_task)
    new_task = new_task +'\n'
    lst[index] = new_task
    with open(filepath, "w") as file:
        for item in lst:
            file.write(item.capitalize())


def complete(filepath, task_to_complete):
        lst = get_lst(filepath)
        index = lst.index(task_to_complete)
        lst.pop(index)
        with open(filepath, "w") as file:
            for item in lst:
                file.write(item.capitalize())



def menu():
    filepath = "tasks.txt"
    while True:
        print("Hello, please select desired action:")
        usr_opt = input("1.Add\n2.Show\n3.Edit\n4.Mark as complete\n5.Close\n")
        if usr_opt == '1':
            task = input("Please input new task:\n")
            add_task(filepath, task)
        elif usr_opt == '2':
            show_list(filepath)
        elif usr_opt == '3':
            tsk_num = input("Please input task number to edit:\n")
            edit_task(filepath, int(tsk_num))
        elif usr_opt == '4':
            tsk_num = input("Please input completed task\n")
            complete(filepath, int(tsk_num))
        elif usr_opt == '5':
            break
        else:
            print("Not a valid option, please try again\n")
