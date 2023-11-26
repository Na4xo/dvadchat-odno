import tkinter as tk
import random
from settings import *

def click():
    global score
    button.configure(text = 'Бери ещё карту!!!')
    while True:
        key = random.choice(list(cards.keys()))
        texts.append(key)
        score += (cards[key])
        break
    print(texts)
    lb_spis.configure(text = texts)
    lb_score.configure(text = score)
    
def deleted():
    global score
    texts.clear()
    lb_spis.configure(text = 'У тебя нет карт,их надо взять')
    score = 0
    lb_score.configure(text = 0)

win = tk.Tk()
win.title('Очко')
win.geometry(f"{W}x{H}")


cards = {'ТУЗ': 11,
               'Десять': 10,
               'Король': 4,
               'Дама': 3,
               'Валет': 2,
               'Девять': 9,
               'Восемь': 8,
               'Семь': 7,
               'Шесть': 6,
               }

score = 0

texts = []

button = tk.Button(bg = COLOR_RED, fg = COLOR_BLUE,font = ('Times New Roman',12), text = "Взять Карту/ Начать игру", command=lambda: click())
button.place(x = 70, y = 60, width = 230, height = 80)

button_2 = tk.Button(bg = COLOR_RED, fg = COLOR_BLUE,font = ('Times New Roman',12),text = 'Руку брось!',command=lambda: deleted())
button_2.place(x = 70,y = 160, width = 230, height = 80)


lb = tk.Label(text='Список карт:', fg = COLOR_RED, font = ('Times New Roman',15))
lb.place(x = 80,y = 250)

lb_spis = tk.Label(text= texts, fg = COLOR_RED, font = ('Times New Roman',10))
lb_spis.place(x = 75,y = 275)

lb_score_sum = tk.Label(text='Очки:', fg = COLOR_RED, font = ('Times New Roman',15))
lb_score_sum.place(x = 80,y = 300)

lb_score = tk.Label(text= score, fg = COLOR_RED, font = ('Times New Roman',10))
lb_score.place(x = 75,y = 327)

win.mainloop()