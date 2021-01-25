from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
import os
import sys
from blackjack_def import*
score_1 = 0
score_2 = 0
def rules():
    rules=Tk()
    rules.geometry("600x800")
    lbl_header = Label(rules, text="Правила игры в Очко", font = "Verdana 30")
    lbl_header.pack()
    lbl_rules = Label(rules, text="Играют одной колодой в 36 карт. Старшинство карт не стандартно\nВалет — 2 очка\nДама — 3 очка\nКороль — 4 очка\nТуз — 11 очков\nОстальные карты при подсчете очков оцениваются по номиналу", font = "Verdana 12")
    lbl_rules.pack()
    lbl_goal = Label(rules, text="Цель игры набрать в сумме 21 очко.", font = "Verdana 25")
    lbl_goal.pack()
    lbl_goal_description = Label(rules, text = "В начале игры определяется банкующий. В нашем случае он выбирается случайным образом из всех участников игры.\nБанкующего выбирает компьютер, потому подтасовка в данном случае невозможна. Колода перемешивается, в нее произвольным образом вставляется закладка, разделяющая колоду на две части.\nКаждый игрок получает на руки по одной карте. После этого каждый может сделать свою ставку.\nПервая ставка — ставка банкующего, то есть банк. Эта ставка является максимально возможной для игрока, сидящего на банке. Банкующий ставит на кон все, что имеет.\n Суммарная ставка всех игроков за столом не может превышать сумму банка.\nВторым ставку делает игрок, сидящий по левую руку от банкующего. Если игра идет на двоих, то игрок может сделать максимальную ставку равную банку.\n В том случае если играют трое, первый игрок может поставить на кон максимум сумму банка минус 1.\n Если игра идет на четверых, ставка первого игрока не может превышать сумму банка минус 2.\n Минимальная ставка любого игрока, играющего против банка 1, даже в случае, если в банке всего 1 фишка.\n Порядок ставок меняется по часовой стрелке.\nСледующим этапом игры банкующий сдает дополнительные карты каждому игроку начиная слева от себя и по часовой стрелке.\nЛюбой игрок в свой ход может попросить дополнительную карту, если считает нужным, или отказаться от нее.\n Игрок может иметь на руках не более 5 карт.\n Игрок, набравший 21 очко, сразу выигрывает.\n Так же сразу выигрывает игрок набравший «золотое очко», то есть имеющий на руках двух тузов.\n Игрок, набравший количество баллов большее чем 21, автоматически проигрывает ставку. Его ставка уходит в банк.\n Игроки набравшие менее 21 очка ждут, пока банкующий не доберет карты себе.\n Если сумма очков банкующего превышает или равна сумме очков игрока, ставка уходит в банк.\n Если сумма очков банкующего меньше суммы очков игрока, ставка плюс выигрыш достаются игроку.\nВ случае если карты до закладки заканчиваются, а игра не закончена, колода перемешивается, ставится новая закладка и игра продолжается.\nОбращаем ваше внимание на то, что вероятность выигрыша в игре «21 очко», как утверждают статисты, достаточно велика — преимущество банка перед игроком менее одного процента.\n Так что стремиться стать банкующим вовсе не обязательно.", font = "Verdana 10")
    lbl_goal_description.pack()
    rules.mainloop()

def exit_def():
    global root
    root.quit()

def count_score():
    global score_11
    number = take_card()
    score_11 = score_11 + number
    lbl_count_you= Label(root, text = score_11,font = "Verdana 40")
    lbl_count_you.grid(row = 7, column = 1)
    if score_11 > 21:
        defeat_def()
    elif score_11 == 21:
        victory()


def start():
    global score_11,score_22
    score_11 = 0
    score_22 = 0
    start_btn.grid_remove()
    rules_btn.grid_remove()
    lbl_lets= Label(root, text = "Начнём игру!", font = "Verdana 20")
    lbl_lets.grid(row = 6, column = 2)
    btn_take= Button(root, command = count_score, text = "Взять карту",width=20, height=3, bg = "grey", fg = "white", font = "Verdana 15")
    btn_take.grid(row = 2,column = 1)
    btn_decline= Button(root, command = ignore, text = "не брать карту",width=20, height=3, bg = "grey", fg = "white", font = "Verdana 15")
    btn_decline.grid(row = 2,column = 2)
    lbl_count_you= Label(root, text = score_11,font = "Verdana 40")
    lbl_count_you.grid(row = 7, column = 1)
    lbl_count_diler= Label(root, text = score_22,font = "Verdana 40")
    lbl_count_diler.grid(row = 7, column = 3)

def ignore():
    global score_22
    score_22 = 0
    score_22 = diler_take_card()
    lbl_count_diler= Label(root, text = score_22,font = "Verdana 40")
    lbl_count_diler.grid(row = 7, column = 3)
    if score_22 > 21:
        victory()
    elif score_22 > score_11:
        defeat_def()
def defeat_def():
    defeat = Tk()
    defeat.geometry("1280x720")
    lbl_defeat= Label(defeat, text = "ВЫ ПРОИГРАЛИ",font = "Verdana 120")
    lbl_defeat.pack(expand=True)
    btn_restart= Button(defeat,command=start, text = "ещё раз",width=30, height=5, bg = "grey", fg = "white", font = "Verdana 15")
    btn_restart.pack(side = "left")
    defeat.mainloop()
def victory():
    win = Tk()
    win.geometry("1280x720")
    lbl_win= Label(win, text = "ВЫ ВЫИГРАЛИ",font = "Verdana 120")
    lbl_win.pack(expand=True)
    btn_restart= Button(win,command=start, text = "ещё раз",width=30, height=5, bg = "grey", fg = "white", font = "Verdana 15")
    btn_restart.pack(side = "left")
    win.mainloop()


root = Tk()
root.title("Blackjack")
root.geometry("1280x720")
greetings = ttk.Label(root, text = "Добро пожаловать в Blackjack!", font = "Verdana 30")
space= Label(root, text = " ", font = "Verdana 30")
lbl_hand_you = ttk.Label(root, text = "Ваша рука", font = "Verdana 20")
lbl_hand_diler = ttk.Label(root, text = "рука дилера", font = "Verdana 20")
start_btn = Button(root, command =start, text = "Начать игру!",width=20, height=3, bg = "grey", fg = "white", font = "Verdana 15")
rules_btn = Button(root, command=rules, text = "Правила", width = 20, height = 3, bg = "grey", fg = "white", font = "Verdana 15" )
exit_btn = Button(root,command=exit_def, text = "выход", width = 20, height = 3, bg = "grey", fg = "white", font = "Verdana 15" )

greetings.grid(row = 0, column = 2, rowspan = 1)
start_btn.grid(row = 2, column = 1,rowspan = 1)
rules_btn.grid(row = 2, column = 2, rowspan = 1)
exit_btn.grid(row = 2,column = 3,rowspan = 1)
space.grid(row = 4, column = 0)
lbl_hand_you.grid(row = 6, column = 1)
lbl_hand_diler.grid(row = 6, column = 3)

root.mainloop()
