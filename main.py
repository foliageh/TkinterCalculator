from tkinter import *

root = Tk()

ent = Entry(width=100)
btn = Button(text="Посчитать", height=3, width=30, bg='aqua', font='arial 26')
lab = Label(bg='black', fg='white', height=3, width=30, font='arial 26')



def strToSortlist(event):
    s = ent.get()
    s.strip()
    if (s.find('*')!=-1):
        zn = '*'
        n1 = float(s[:s.find(zn)])
        n2 = float(s[s.find(zn) + 1:])
        ans = n1 * n2
    elif (s.find('+')!=-1):
        zn = '+'
        n1 = float(s[:s.find(zn)])
        n2 = float(s[s.find(zn) + 1:])
        ans = n1 + n2
    elif (s.find('-')!=-1):
        zn = '-'
        n1 = float(s[:s.find(zn)])
        n2 = float(s[s.find(zn) + 1:])
        ans = n1 - n2
    elif (s.find('^')!=-1):
        zn = '^'
        n1 = float(s[:s.find(zn)])
        n2 = float(s[s.find(zn) + 1:])
        ans = n1 ** n2
    else:
        zn = '/'
        n1 = float(s[:s.find(zn)])
        n2 = float(s[s.find(zn) + 1:])
        if n2 != 0:
            ans = n1 / n2
        else:
            ans = 'НА 0 ДЕЛИТЬ НЕЛЬЗЯ, ДЕБИЛЫ!'
    if ans == 'НА 0 ДЕЛИТЬ НЕЛЬЗЯ, ДЕБИЛЫ!':
        lab['text'] = str(ans)
    else:
        lab['text'] = ent.get()+'='+str(ans)


btn.bind('<Button-1>', strToSortlist)
ent.bind('<Return>', strToSortlist)

ent.grid(row=1, column=0)
btn.grid(row=2, column=0)
lab.grid(row=3, column=0)

root.mainloop()
