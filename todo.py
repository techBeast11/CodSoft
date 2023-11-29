import tkinter as tk
from tkinter import messagebox

def add_task_to_list():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def update_selected_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        updated_task = task_entry.get()
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(selected_task_index, updated_task)
        task_entry.delete(0, tk.END)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

def delete_selected_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

root = tk.Tk()
root.title("To-Do List")

root.geometry("400x400")

task_label = tk.Label(root, text="Enter Task:")
task_label.pack(pady=10)
task_entry = tk.Entry(root, width=40)
task_entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task_to_list)
add_button.pack(pady=5)

update_button = tk.Button(root, text="Update Task", command=update_selected_task)
update_button.pack(pady=5)

tasks_label = tk.Label(root, text="Tasks:")
tasks_label.pack()
tasks_listbox = tk.Listbox(root, width=40, height=10)
tasks_listbox.pack(pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_selected_task)
delete_button.pack(pady=5)

root.mainloop()
