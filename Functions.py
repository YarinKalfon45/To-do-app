"""
Functions File
"""

from datetime import datetime


def showtime():
    """
    A function that shows current time for GUI version
    :return: current time and date
    """
    now = datetime.now()
    date_str = now.strftime("%d/%m/%Y")
    time_str = now.strftime('%H:%M:%S')
    print(f"Today is {date_str}, The current time is {time_str}")
    return now


def get_lst(filepath):
    """
    A function that returns the list of our tasks
    :param filepath: txt file with all the tasks
    :return: list with all the tasks
    """
    with open(filepath, "r") as file:
        lst = file.readlines()  # Each line turns into element in the list
        return lst


def show_list(filepath):
    """
    This function Shows the list of tasks
    :param filepath: txt file with all the tasks
    :return:
    """
    print("Your tasks for today are:")
    lst = get_lst(filepath)
    for i in range(len(lst)):
        print(f"{i + 1}.{lst[i]}")
    print("\n", end='')


def add_task(filepath, task):
    """
    A function that adds a new task
    :param filepath: txt file with all the tasks
    :param task: the task wich we want to add
    :return:
    """
    with open(filepath, "a") as file:
        file.write(task.capitalize() + '\n')  # Writing The new task at the end of the file


def edit_task(filepath, old_task, new_task):
    """
    A function that edits an exiting task
    :param filepath: txt file with all the tasks
    :param old_task: the task we want to edit
    :param new_task: the new task to replace it
    :return:
    """
    lst = []
    lst = get_lst(filepath)  # Getting the list
    index = lst.index(old_task)  # Finding the index of the task we want to change
    new_task = new_task + '\n'  # Adding '/n' so the file format stays the same
    lst[index] = new_task  # Replacing the old task with the edited task
    with open(filepath, "w") as file:
        for item in lst:
            file.write(item.capitalize())  # Writing the new list into the file


def complete(filepath, task_to_complete):
    """
    A function that enables to mark task as completed an remove it from the tasks list
    :param filepath: txt file with all the tasks
    :param task_to_complete: the task we completed
    :return:
    """
    lst = get_lst(filepath)  # Getting the list
    index = lst.index(task_to_complete)   # Finding the index of the task we want to remove
    lst.pop(index)  # Removing the task
    with open(filepath, "w") as file:
        for item in lst:
            file.write(item.capitalize())  # Writing the updated list to the file


def menu():
    """
    This is a CLI version to check the functions
    :return:
    """
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
