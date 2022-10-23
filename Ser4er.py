from tkinter import *

from PIL import Image, ImageTk

screen = Tk()

screen.resizable(width=False,height=False)
screen.geometry("300x350")
screen.title("Ser4er")
screen.iconbitmap("sys\\icons\\icon.ico")

color_1="black"
color_2="white"
screen["bg"]=color_2
file = None

def search():
    text.delete(1.0, END)
    word = ent.get().lower()
    with open(f"data\\words\\words_{file}.txt","r",encoding="utf-8") as f:
        data = f.readlines()
    answer=""
    for i in data:
        if word in i:
            answer+=f"{i}\n"
    if answer=="":
        answer="No result"

    text.insert(1.0,answer)

ent = Entry(screen,
    justify="center",font="20",bg=color_2,fg=color_1)
ent.place(width=200,height=27,x=53,y=5)

text = Text(wrap=WORD,font="20",bg=color_2,fg=color_1)
text.place(width=275,height=250, x=10,y=80)


scroll = Scrollbar(command=text.yview)
scroll.place(width=15,height=250,x=285,y=80)

text.config(yscrollcommand=scroll.set)


b_search = Button(text="Search",
    fg=color_1,
    bg=color_2,
    activebackground=color_1,
    activeforeground=color_2,
    command=search,
    )
b_search.place(width = 80,height=25 ,x=110,y=40)

var = IntVar()
var.set(0)
eng = Radiobutton(text="English",
                  variable=var, value=0)
tur = Radiobutton(text="Turkey",
                  variable=var, value=1)
eng.place(x=70,y=20)
tur.place(x=240,y=20)




screen.mainloop()