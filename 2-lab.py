import redis
import tkinter.ttk as ttk
import tkinter as tk
from tkinter import font
from tkinter import colorchooser
import json

# Подключение к БД
with open('host', 'r') as file:
    HOST = file.read()
with open('passwd', 'r') as file:
    PASSWORD = file.read()
client = redis.StrictRedis(host=HOST, password=PASSWORD) 

# Префикс для уникальности ключей, чтобы совместно работать в БД
MY_PREFIX = "poskitt_22304_"

# Создание основного окна и установка его заголовка    
root = tk.Tk()
root.title("Монитор спортивных соревнований")

SCR_WIDTH = root.winfo_screenwidth() 
SCR_HEIGHT = root.winfo_screenheight()
root.geometry(f"{SCR_WIDTH}x{SCR_HEIGHT}")

# Переменные для динамичского изменения настроек текста
curr_judge = tk.StringVar()
curr_sportsman = tk.StringVar()
given_score = tk.StringVar()

# Список судей и спортсменов соответственно
judges = ("Mr. Red", "Mr. Green", "Mr. Blue")
sportsmans = ("Faster", "Higher", "Stronger")

# Выбор судьи
judge_lbl = tk.Label(root, text="Судья:").pack(pady=10)

judge_combo = ttk.Combobox(root, values=judges, textvariable=curr_judge, state="readonly")
judge_combo.current(0)
judge_combo.pack()

# Выбор спортсмена
sportsman_lbl = tk.Label(root, text="Спортсмен:").pack(pady=10)

sportsman_combo = ttk.Combobox(root, values=sportsmans, textvariable=curr_sportsman, state="readonly")
sportsman_combo.current(0)
sportsman_combo.pack()

# Выставление баллов
sportsman_lbl = tk.Label(root, text="Выставить баллы:").pack(pady=10)

score_entry = tk.Entry(root, textvariable=given_score)
score_entry.pack()

# Сохранение выставленного балла
save_score = tk.Button(root, text="Сохранить")
save_score.pack(pady=10)

# Рейтинг-лист
columns = ("Surname", "Score")
rating_tree = ttk.Treeview(root, columns=columns, show="headings")
rating_tree.heading("Surname", text="Фамилия")
rating_tree.heading("Score", text="Сумма баллов")

for sp in sportsmans:
    rating_tree.insert("", "end", values=(sp, 0))
rating_tree.pack(pady=10)

# Передача управления пользователю
root.mainloop()