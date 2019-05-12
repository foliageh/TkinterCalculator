from tkinter import *
from math import *
root = Tk()

ent = Entry(width=100)
btn = Button(text="Посчитать", height=3, width=30, bg='aqua', font='arial 26')
lab = Label(bg='black', fg='white', height=3, width=30, font='arial 26')


def strToSortlist(event):
    s = ent.get()
    s = s.replace(' ', '')
    s0 = s
    s = s.replace('^', '**')
    try:
        ans = str(eval(s))
        lab['text'] = s0 + '=' + ans
        if len(lab['text']) > 31:
            lab['text'] = ans
    except:
        lab['text'] = 'НЕКОРРЕКТНОЕ ВЫРАЖЕНИЕ!'


btn.bind('<Button-1>', strToSortlist)
ent.bind('<Return>', strToSortlist)
ent.grid(row=1, column=0)
btn.grid(row=2, column=0)
lab.grid(row=3, column=0)

root.mainloop()
