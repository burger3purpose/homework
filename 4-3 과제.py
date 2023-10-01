import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)

window = tk.Tk()
window.title("To-Do List")
window.geometry("250x250")

label1 = tk.Label(window, text = 'Add a Task:')
label1.pack()

entry = tk.Entry(window, width=40)
entry.pack()

add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack()

task_list = tk.Listbox(window, selectmode=tk.SINGLE, width=40)
task_list.pack()

delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack()

window.mainloop()