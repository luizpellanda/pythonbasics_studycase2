# Daily Task Manager
# A console-based organizational tool for managing personal to-do lists.

# Inputs: User commands via an interactive menu to Add, View, or Remove tasks.

# Logic:

# Use a list structure to persist task entries during the session.

# Implement input validation to handle empty entries or invalid selection indices.

# Outputs: Updated list state or confirmation messages for performed operations.

import os
import sys

tasks = [{'task': 'Homework', 'status': False}]

def show_program_name():
    print('''
          Super Awesome Task Manager
        ''')

def show_menu():
    print('1. Create Task')
    print('2. View Tasks')
    print('3. Complete a Task')
    print('4. Remove Task')
    print('5. Exit\n')

def return_to_menu():
    input('\nPress Enter to go back to main menu...')

def clear_and_print(message):
    os.system('cls' if os.name == 'nt' else 'clear')
    line = '*' * len(message)
    print(line)
    print(message)
    print(line + '\n')

def invalid_option():
    print('Invalid option. Please select a valid option.')
    return_to_menu()

def handle_user_selection():
    try:
        chosen_option = int(input('Select an option: '))
        match chosen_option:
            case 1:
                create_task()
            case 2:
                view_tasks_page()
            case 3:
                change_task_status()
            case 4:
                remove_task()
            case 5:
                end_app()
            case _:
                invalid_option()
    except ValueError:
        invalid_option()

def end_app():
    clear_and_print('Closing Task Manager. See you!')
    sys.exit()

def list_tasks_function():
    print(f"{'#'.ljust(4)} | {'Task'.ljust(25)} | {'Status'.ljust(12)}\n")
    for index, task in enumerate(tasks, start=1):
        task_name = task['task']
        task_status = 'Complete' if task['status'] else 'Incomplete'
        print(f'  {str(index).ljust(3)}| {task_name.ljust(25)} | {task_status.ljust(12)}')

def create_task():
    clear_and_print('--- Create Task ---')
    task_name = input('Task name: ')
    if not task_name.strip():
        print('Task name cannot be empty.')
        return_to_menu()
        return
    tasks.append({'task': task_name, 'status': False})
    print(f'Task "{task_name}" created successfully!')
    return_to_menu()

def view_tasks_page():
    clear_and_print('--- Task List ---')
    list_tasks_function()
    return_to_menu()

def change_task_status():
    while True:
        clear_and_print('--- Complete a Task ---')
        list_tasks_function()
        task_name = input('\nTask name: ')
        found = False
        for task in tasks:
            if task['task'] == task_name:
                found = True
                task['status'] = True
                print(f'Task "{task_name}" marked as complete!')
        if not found:
            print('Task not found! Check the spelling.')
        choice = input('\n[1] Complete another task\n[2] Back to main menu\n\nOption: ')
        if choice == '2':
            break

def remove_task():
    while True:
        clear_and_print('--- Remove Task ---')
        list_tasks_function()
        task_name = input('\nTask name: ')
        found = False
        for task in tasks:
            if task['task'] == task_name:
                found = True
                tasks.remove(task)
                print(f'Task "{task_name}" removed successfully!')
                break
        if not found:
            print('Task not found! Check the spelling.')
        choice = input('\n[1] Remove another task\n[2] Back to main menu\n\nOption: ')
        if choice == '2':
            break

def main():
    while True:
        show_program_name()
        show_menu()
        handle_user_selection()

if __name__ == '__main__':
    main()