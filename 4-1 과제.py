import tkinter as tk
from tkinter import PhotoImage

def show_image():
    selected_animal = image_selection.get()
    image_path = ""

    if selected_animal == "강아지":
        image_path = r"C:\Users\sam03\OneDrive\바탕 화면\2학기 프로그래밍\사진 zip\dog.gif"
    elif selected_animal == "고양이":
        image_path = r"C:\Users\sam03\OneDrive\바탕 화면\2학기 프로그래밍\사진 zip\cat.gif"
    elif selected_animal == "토끼":
        image_path = r"C:\Users\sam03\OneDrive\바탕 화면\2학기 프로그래밍\사진 zip\rabbit.gif"

    img = PhotoImage(file=image_path)
    image_label.config(image=img)
    image_label.image = img

window = tk.Tk()
window.geometry("250x400")
window.title("애완동물 선택하기")

label2 = tk.Label(window, text = '좋아하는 동물 투표', fg = 'blue')
label2.pack()

image_selection = tk.StringVar(value="강아지")

radio_button_dog = tk.Radiobutton(window, text="강아지", variable=image_selection, value="강아지")
radio_button_cat = tk.Radiobutton(window, text="고양이", variable=image_selection, value="고양이")
radio_button_rabbit = tk.Radiobutton(window, text="토끼", variable=image_selection, value="토끼")

radio_button_dog.pack()
radio_button_cat.pack()
radio_button_rabbit.pack()

image_label = tk.Label(window)
image_label.pack()

show_image_button = tk.Button(window, text="사진보기", command=show_image)
show_image_button.pack()

window.mainloop()