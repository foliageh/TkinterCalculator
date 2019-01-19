from tkinter import *

root = Tk()

ent = Entry(width=100)
#ent1 = Entry(width=100)
btn = Button(text="Посчитать", height=3, width=30, bg='aqua', font='arial 26')
lab = Label(bg='black', fg='white', height=3, width=30, font='arial 26')
# chb = Checkbutton(text="Поставьте галочку")
# sck = Scale()


def strToSortlist(event):
    s = ent.get()
    s.strip()
    if (s.find('*')!=-1):
        zn = '*'
        n1 = int(s[:s.find(zn)])
        n2 = int(s[s.find(zn) + 1:])
        ans = n1 * n2
    elif (s.find('+')!=-1):
        zn = '+'
        n1 = int(s[:s.find(zn)])
        n2 = int(s[s.find(zn) + 1:])
        ans = n1 + n2
    elif (s.find('-')!=-1):
        zn = '-'
        n1 = int(s[:s.find(zn)])
        n2 = int(s[s.find(zn) + 1:])
        ans = n1 - n2
    elif (s.find('^')!=-1):
        zn = '^'
        n1 = int(s[:s.find(zn)])
        n2 = int(s[s.find(zn) + 1:])
        ans = n1 ** n2
    else:
        zn = '/'
        n1 = int(s[:s.find(zn)])
        n2 = int(s[s.find(zn) + 1:])
        ans = n1/n2
    #s = s.split()
    #s.sort()
    lab['text'] = ent.get()+'='+str(ans)


btn.bind('<Button-1>', strToSortlist)


# ent1.grid(row=0, column=0)
ent.grid(row=1, column=0)
btn.grid(row=2, column=0)
lab.grid(row=3, column=0)
# chb.grid(row=0, column=0)
# sck.grid(row=0, column=0)

root.mainloop()
