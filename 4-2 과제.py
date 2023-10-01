import tkinter as tk

strings = [
    "jeju1.gif",
    "jeju2.gif",
    "jeju3.gif",
    "jeju4.gif",
    "jeju5.gif",
    "jeju6.gii",
    "jeju7.gif",
    "jeju8.gif",
    "jeju9.gif",
]
current_index = 0


def show_previous_string():
    global current_index
    current_index -= 1
    if current_index < 0:
        current_index = len(strings) - 1
    show_string()

def show_next_string():
    global current_index
    current_index += 1
    if current_index >= len(strings):
        current_index = 0
    show_string()

def show_string():
    string_label.config(text=strings[current_index])

window = tk.Tk()
window.title("tk")
window.geometry("400x100")

string_label = tk.Label(window, text="", fg = 'blue')
string_label.pack()

previous_button = tk.Button(window, text="<이전>", command=show_previous_string)
previous_button.pack(side = "left")

next_button = tk.Button(window, text="<다음>", command=show_next_string)
next_button.pack(side = "right")

show_string()

window.mainloop()