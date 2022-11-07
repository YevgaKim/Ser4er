from functools import partial
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

from parse_quizlet_tur import get_tur_or_eng
from parse_word_eng import get_eng

screen = Tk()

screen.resizable(width=False,height=False)
screen.geometry("300x370")
screen.title("Ser4er")
screen.iconbitmap("sys\\icons\\icon.ico")

color_1="black"
color_2="white"
screen["bg"]=color_2
FILE = ""

def parse_tur_or_eng(count):
    title_lan=""
    if count==0:
        lan="en"
        file="eng"
        title_lan="English"
    elif count==1:
        lan="tr"
        file="tur"
        title_lan="Turkish"
    mb.showinfo(
        title=title_lan, 
        message="Parsing started. Just wait")
    try:
        get_tur_or_eng(lan,file)
    except:
        mb.showerror(
            "Error", 
            "ERROR")

    mb.showinfo(
        title=title_lan, 
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


def search(ev):
    if var.get() == 0:
        FILE="eng"
    elif var.get() == 1:
        FILE = 'tur'
    text.delete(1.0, END)
    word = ent.get().lower().strip()
    with open(f"data\\words\\words_{FILE}.txt","r",encoding="utf-8") as f:
        data = f.readlines()
    answer=""
    for i in data:
        if word in i:
            answer+=f"{i}======================\n"
    if answer=="":
        answer="-----------------No result-----------------"

    text.insert(1.0,answer)


ent = Entry(screen,
    justify="center",font="20",bg=color_2,fg=color_1)
ent.place(width=200,height=27,x=53,y=5)

text = Text(wrap=WORD,font="20",bg=color_2,fg=color_1)
text.place(width=275,height=260, x=10,y=80)


scroll = Scrollbar(command=text.yview)
scroll.place(width=15,height=260,x=285,y=80)

text.config(yscrollcommand=scroll.set)

search_2 = partial(search,"")
b_search = Button(text="Search",
    fg=color_1,
    bg=color_2,
    activebackground=color_1,
    activeforeground=color_2,
    command=search_2,
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

parsemenu = Menu(mainmenu, tearoff=0)
helpmenu2 = Menu(parsemenu, tearoff=0)

parse_eng2 = partial(parse_tur_or_eng,0)
parse_tur = partial(parse_tur_or_eng,1)

helpmenu2.add_command(
    label="English",command=parse_eng2)
helpmenu2.add_command(
    label="Turkish",command=parse_tur)
 
parsemenu.add_cascade(label="Quizlet",
                     menu=helpmenu2)



parsemenu.add_command(label="English", command=parse_eng)

mainmenu.add_cascade(label="Parse",
                    menu=parsemenu)

screen.bind('<Return>', search)
keyboard= ["q","w","e","r","t","y","u","i","o","p",
            "a","s","d","f","g","h","j","k","l",
            "z","x","c","v","b","n","m"]
for i in keyboard:
    screen.bind(i,search)

screen.bind('<BackSpace>', search)

screen.mainloop()
