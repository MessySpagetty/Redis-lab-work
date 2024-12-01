import redis
import tkinter.ttk as ttk
import tkinter as tk
from tkinter import font
from tkinter import colorchooser
import json


def print_set(sorted_set):
    ascending = client.zrange(sorted_set, 0, -1, withscores=True)
    print(ascending)


def save_results(judge, sporsman, score):
    raise NotImplementedError


def update_leaderbord(judges, sportsmans):
    for ju in judges:
        client.zadd(MY_PREFIX + ju, sportsmans)
    print_set(MY_PREFIX + ju)

def init_tree(sportsmans):
    columns = ("Surname", "Score")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    tree.heading("Surname", text="Фамилия")
    tree.heading("Score", text="Сумма баллов")
    for sp in sportsmans.keys():
        tree.insert("", "end", values=(sp, sportsmans[sp]))
    return tree


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
sportsmans = {"Faster": 0, "Higher": 0, "Stronger": 0}

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
save_score = tk.Button(root, text="Сохранить", command=save_results)
save_score.pack(pady=10)

# Рейтинг-лист
rating_tree = init_tree(sportsmans)
rating_tree.pack()


update_leaderbord(judges, sportsmans)

# Передача управления пользователю
root.mainloop()
