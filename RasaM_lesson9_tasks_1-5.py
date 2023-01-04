# Sukurti programą su grafine sąsaja, kuri:
# Turėtų laukelį su užrašu "Įveskite vardą", kuriame vartotojas galėtų įvesti vardą
# Turėtų mygtuką su užrašu "Patvirtinti", kurį nuspaudus, programa po lauku atspausdintų "Labas, {vardas}!"

from tkinter import *

window = Tk()

def say_hello():
    is_inserted = insert1.get()
    label2["text"] = (f"Labas, {is_inserted}!")

# Configuration of labels and buttons
label1 = Label(window, text="Įveskite vardą")
insert1 = Entry(window)
button_patvirtinti = Button(window, text="Patvirtinti", command = say_hello)
label2 = Label(window, text="")

# Drow window
label1.grid(row=0, column=0)
insert1.grid(row=0, column=1)
button_patvirtinti.grid(row=0, column=2)
label2.grid(row=1, columnspan=3)
window.mainloop()


# Patobulinti 1 užduoties programą, kad ji:
# Įvedus vardą, atspausdintų "Labas, {vardas}!" ne tik nuspaudus mygtuką, bet ir paspaudus mygtuką "Enter"


from tkinter import *

main_window = Tk()

def say_hello():
    is_inserted = insert1.get()
    label2["text"] = (f"Labas, {is_inserted}!")




# Configuration of labels and buttons
label1 = Label(main_window, text="Įveskite vardą")
insert1 = Entry(main_window)
button_patvirtinti = Button(main_window, text="Patvirtinti", command=say_hello)
# Configure pres enter
insert1.bind("<Return>", lambda event: say_hello())
label2 = Label(main_window, text="")

# Drow window
label1.grid(row=0, column=0)
insert1.grid(row=0, column=1)
button_patvirtinti.grid(row=0, column=2)
label2.grid(row=1, columnspan=3)
main_window.mainloop()

# Patobulinti 2 užduoties programą, kad ji:
# Turėtų meniu, kuriame:
# Būtų punktas "Išvalyti", kurį paspaudus išsitrintų tekstas eilutėje, kurioje spausdinamas pasisveikinimo tekstas
# Būtų punktas "Atkurti", kurį paspaudus pasisveikinimo teksto eilutėje butų atspausdintas paskutinis atspausdintas tekstas
# Būtų punktas "Išeiti", kurį paspaudus užsidarytų programos window
# Tarp menių punktų "Atkurti" ir "Išeiti" būtų atskyrimo brūkšnys


from tkinter import *

main_window = Tk()
last_of = StringVar()

def say_hello():
    is_inserted = insert1.get()
    label2["text"] = (f"Labas, {is_inserted}!")
    last_of.set(label2["text"])

def clean():
    label2["text"] = ""

def undo():
    label2["text"] = last_of.get()

def exit_of():
    main_window.destroy()

# Configuration of labels and buttons
label1 = Label(main_window, text="Įveskite vardą")
insert1 = Entry(main_window)
button_patvirtinti = Button(main_window, text="Patvirtinti", command=say_hello)
insert1.bind("<Return>", lambda event: say_hello())
label2 = Label(main_window, text="")

# Meniu:
meniu = Menu(main_window)
main_window.config(menu=meniu)
submeniu = Menu(meniu, tearoff = 0)
meniu.add_cascade(label="Meniu", menu=submeniu)

submeniu.add_command(label="Išvalyti", command = clean)
submeniu.add_command(label="undo paskutinį", command = undo)
submeniu.add_separator()
submeniu.add_command(label="Išeiti", command = exit_of)

# Drow window
label1.grid(row=0, column=0)
insert1.grid(row=0, column=1)
button_patvirtinti.grid(row=0, column=2)
label2.grid(row=1, columnspan=3)
main_window.mainloop()

# Patobulinti 3 užduoties programą, kad ji:
# Turėtų statuso juostą apačioje, kurioje:
# Būtų rodoma "Sukurta", kai atspausdinamas pasisveikinimo tekstas
# Būtų rodoma "Išvalyta", kai ištrinamas pasisveikinimo tekstas
# Būtų rodoma "Atkurta", kai atkuriamas last_of pasisveikinimo tekstas
# Nuspaudus klaviatūros mygtuką "Escape", uždarytų programos langą

from tkinter import *

window = Tk()
last_of = StringVar()

def say_hello():
    is_inserted = insert1.get()
    label2["text"] = (f"Labas, {is_inserted}!")
    last_of.set(label2["text"])
    status["text"] = "Sukurta"

def clean():
    label2["text"] = ""
    status["text"] = "Išvalyta"

def undo():
    label2["text"] = last_of.get()
    status["text"] = "Atkurta"

def exit_of():
    window.destroy()

# Configuration of labels and buttons
label1 = Label(window, text="Įveskite vardą")
insert1 = Entry(window)
button_patvirtinti = Button(window, text="Patvirtinti", command=say_hello)
insert1.bind("<Return>", lambda event: say_hello())
label2 = Label(window, text="")
window.bind("<Escape>", lambda event: exit_of())


# Status 
status = Label(window, text="", bd=1, relief=SUNKEN, anchor=W)

# Drow window
label1.grid(row=0, column=0)
insert1.grid(row=0, column=1)
button_patvirtinti.grid(row=0, column=2)
label2.grid(row=1, columnspan=3)
status.grid(row=2, columnspan=3, sticky=W+E)

# Meniu:
meniu = Menu(window)
window.config(menu=meniu)
submeniu = Menu(meniu, tearoff = 0)
meniu.add_cascade(label="Meniu", menu=submeniu)

submeniu.add_command(label="Išvalyti", command = clean)
submeniu.add_command(label="undo paskutinį", command = undo)
submeniu.add_separator()
submeniu.add_command(label="Išeiti", command = exit_of)

# Drow window
label1.grid(row=0, column=0)
insert1.grid(row=0, column=1)
button_patvirtinti.grid(row=0, column=2)
label2.grid(row=1, columnspan=3)
status.grid(row=2, columnspan=3, sticky=W+E)
window.mainloop()

# Perdaryti bet kurią ankstesnėse pamokose sukurtą programą, kurioje vartotojas turėjo įvesti duomenis, į programą su grafine sąsaja

from tkinter import *
import calendar

window = Tk()

def check():
    is_inserted = int(insert1.get())
    if calendar.isleap(is_inserted):
        label2["text"] = (f"{is_inserted} metai yra keliamieji!")
    else:
        label2["text"] = (f"{is_inserted} metai yra nekeliamieji!")

def exit_of():
    window.destroy()

# Configuration of labels and buttons
label1 = Label(window, text="Įveskite metus")
insert1 = Entry(window)
button_patvirtinti = Button(window, text="Patvirtinti", command=tikrinti)
insert1.bind("<Return>", lambda event: check())
window.bind("<Escape>", lambda event: exit_of())
label2 = Label(window, text="")

# Drow window
label1.grid(row=0, column=0)
insert1.grid(row=0, column=1)
button_patvirtinti.grid(row=0, column=2)
label2.grid(row=1, columnspan=3)
window.mainloop()