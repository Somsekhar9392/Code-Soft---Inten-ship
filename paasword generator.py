import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store tasks
FILE_NAME = 'tasks.json'

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file)

# Add a task
def add_task():
    title = entry_task.get()
    if title:
        tasks.append({'title': title, 'done': False})
        entry_task.delete(0, tk.END)
        update_listbox()
        save_tasks(tasks)
    else:
        messagebox.showwarning("Warning", "Task title cannot be empty!")

# Update the status of a task
def toggle_task(event):
    selected_task_index = listbox_tasks.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        tasks[index]['done'] = not tasks[index]['done']
        update_listbox()
        save_tasks(tasks)

# Update the Listbox with tasks
def update_listbox():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        status = 'Done' if task['done'] else 'Not Done'
        listbox_tasks.insert(tk.END, f"{task['title']} - {status}")

# Initialize main window
root = tk.Tk()
root.title("To-Do List")

# Create and place widgets
frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

listbox_tasks = tk.Listbox(frame_tasks, width=50, height=10, selectmode=tk.SINGLE)
listbox_tasks.pack(side=tk.LEFT)

                                               

scrollbar = tk.Scrollbar(frame_tasks, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=10)

button_add_task = tk.Button(root, text="Add Task", command=add_task)
button_add_task.pack(pady=5)

listbox_tasks.bind("<Double-1>", toggle_task)

# Load and display tasks
tasks = load_tasks()
update_listbox()

root.mainloop()
