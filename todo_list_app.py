import tkinter as tk
from tkinter import messagebox
import json

# File to store tasks
TASKS_FILE = "tasks.json"

# Function to load tasks from file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

# Add new task
def add_task():
    task = task_entry.get()
    
    if not task:
        messagebox.showerror("Input Error", "Task cannot be empty.")
        return
    
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    update_task_list()
    task_entry.delete(0, tk.END)

# Edit an existing task
def edit_task():
    selected_task = task_listbox.curselection()
    if not selected_task:
        messagebox.showwarning("Selection Error", "Please select a task to edit.")
        return
    
    task = tasks[selected_task[0]]
    task_entry.delete(0, tk.END)
    task_entry.insert(0, task['task'])
    delete_task()

# Delete a task
def delete_task():
    selected_task = task_listbox.curselection()
    if not selected_task:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")
        return
    
    task = tasks[selected_task[0]]
    tasks.remove(task)
    save_tasks(tasks)
    update_task_list()

# Mark a task as completed
def mark_completed():
    selected_task = task_listbox.curselection()
    if not selected_task:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")
        return
    
    task = tasks[selected_task[0]]
    task["completed"] = True
    save_tasks(tasks)
    update_task_list()

# Update the list of tasks in the Listbox
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        display_text = task['task']
        if task['completed']:
            display_text = f"[Completed] {display_text}"
        task_listbox.insert(tk.END, display_text)

# Initialize the main application window
app = tk.Tk()
app.title("To-Do List")
app.geometry("500x400")

# Load existing tasks from file
tasks = load_tasks()

# Create input fields and labels
task_label = tk.Label(app, text="Task:")
task_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
task_entry = tk.Entry(app)
task_entry.grid(row=0, column=1, padx=10, pady=5)

# Create buttons
add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.grid(row=1, column=0, padx=10, pady=10)

edit_button = tk.Button(app, text="Edit Task", command=edit_task)
edit_button.grid(row=1, column=1, padx=10, pady=10)

delete_button = tk.Button(app, text="Delete Task", command=delete_task)
delete_button.grid(row=1, column=2, padx=10, pady=10)

completed_button = tk.Button(app, text="Mark as Completed", command=mark_completed)
completed_button.grid(row=2, column=0, padx=10, pady=10)

# Create listbox to display tasks
task_listbox = tk.Listbox(app, width=50, height=10)
task_listbox.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Populate the listbox with existing tasks
update_task_list()

# Start the Tkinter event loop
app.mainloop()
