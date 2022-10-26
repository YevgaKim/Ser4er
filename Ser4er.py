from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

from PIL import Image, ImageTk

from sys.parse_quizlet_tur import get_tur
from sys.parse_word_eng import get_eng

screen = Tk()

screen.resizable(width=False,height=False)
screen.geometry("300x370")
screen.title("Ser4er")
screen.iconbitmap("sys\\icons\\icon.ico")

color_1="black"
color_2="white"
screen["bg"]=color_2
file = ""

def parse_tur():
    mb.showinfo(
        title="Turkish", 
        message="Parsing started. Just wait")
    try:
        get_tur()
    except:
        mb.showerror(
            "Error", 
            "ERROR")

    mb.showinfo(
        title="Turkish", 
        message="Parsing finished")

def parse_eng():
    file_name = fd.askopenfilename()
    mb.showinfo(
        title="English", 
        message="Parsing started. Just wait")
    try:
        get_eng(file_name)
    except:
        mb.showerror(
            "Error", 
            "ERROR")

    mb.showinfo(
        title="English", 
        message="Parsing finished")


def search():
    if var.get() == 0:
        file="eng"
    elif var.get() == 1:
        file = 'tur'
    text.delete(1.0, END)
    word = ent.get().lower().strip()
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
text.place(width=275,height=260, x=10,y=80)


scroll = Scrollbar(command=text.yview)
scroll.place(width=15,height=260,x=285,y=80)

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
                  variable=var, value=0
                  ,bg=color_2)

tur = Radiobutton(text="Turkish",
                  variable=var, value=1
                  ,bg=color_2)

eng.place(x=30,y=40)
tur.place(x=210,y=40)

mainmenu = Menu(screen) 
screen.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Turkish",command=parse_tur)
filemenu.add_command(label="English", command=parse_eng)
 
mainmenu.add_cascade(label="Parse",
                     menu=filemenu)



screen.mainloop()