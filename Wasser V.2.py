from tkinter import *
import tkinter as tk  
from functools import partial
from tkinter import messagebox
import time
# Ereignisverarbeitung

def buttonVerarbeitenClick():
    listeAusgewaehlt = listboxNamen.curselection()
    itemAusgewaehlt = listeAusgewaehlt[0]
    nameAusgewaehlt = listboxNamen.get(itemAusgewaehlt)
    textBegruessung = nameAusgewaehlt
    labelText.config(text=textBegruessung)
    if(textBegruessung=='Männlich'):
        m = Label(tkFenster, text="Du solltest pro Tag \n 3 Liter Wasser trinken") 
        m.place(x=10, y= 160)
        liter = 3
    if(textBegruessung=='Weiblich'):
        w = Label(tkFenster, text="Du solltest pro Tag \n 2,5 Liter Wasser trinken") 
        w.place(x=10, y= 160)
        liter = 2,5

def show_entry():
    num1 = (eingabe1.get())  
    num2 = (eingabe2.get()) 
    ausgabe = liter-(int(num1)+int(num2)) 
    wasser = Label(tkFenster, text=ausgabe)
    wasser.place(x=130, y= 130)


# Erzeugung des Fensters
tkFenster = Tk()
tkFenster.title('Test')
tkFenster.geometry('220x300')
#Ausrechnen
number1 = tk.StringVar()  
number2 = tk.StringVar()  
eingabe1 = Entry(tkFenster, textvariable=number1)
eingabe1.place(width = 50, x=120, y=30)
eingabe2 = Entry(tkFenster, textvariable=number2)
eingabe2.place(width = 50, x=120, y=50)
Button(tkFenster, text='Show', command=show_entry).place(x=130, y=100)
# Rahmen Listbox
frameListbox = Frame(master=tkFenster)
frameListbox.place(x=5, y=5, width=110, height=80)
# Rahmen Ausgabe
frameAusgabe = Frame(master=tkFenster)
frameAusgabe.place(x=5, y=90, width=110, height=30)
# Rahmen Verarbeitung
frameVerarbeitung = Frame(master=tkFenster)
frameVerarbeitung.place(x=5, y=125, width=110, height=30)
# Kontrollvariable
text = StringVar()
# Listbox
listboxNamen = Listbox(master=frameListbox, selectmode='browse')
listboxNamen.insert('end', 'Männlich')
listboxNamen.insert('end', 'Weiblich')
listboxNamen.place(x=5, y=5, width=100, height=70)
# Label Text
labelText = Label(master=frameAusgabe, bg='white')
labelText.place(x=5, y=5, width=100, height=20)
# Button verarbeiten
buttonVerarbeiten = Button(master=frameVerarbeitung, text='Bestätigen', command=buttonVerarbeitenClick)
buttonVerarbeiten.place(x=5, y=5, width=100, height=20)

#Menüleite und Zeit

def Zähler(counter = 0):
    counter += 1
    Aktuell = time.ctime()
    DatumZeit.config(text=Aktuell)
    tkFenster.after (1000, Zähler, counter)

def Fenster_Inhalt():
    Aktuell = time.ctime()
    DatumZeit.config(text=Aktuell)


DatumZeit = Label(tkFenster, font=("Arial 10 bold"),
              width=1,
              height=1, bg="white",
              fg="black",
              text="OK")
DatumZeit.place(x=120, y=0, width=100, height=15)

Fenster_Inhalt()
Zähler()

def button_action():
        call_result()
        print("Ein Ergebnis wurde ausgegeben ohne Fehlern")
        
def action_get_info_dialog():
	m_text = "\
************************\n\
Autor: Tom Joeres\n\
Date: 3.05.2021\n\
Version: 1.2\n\
************************"
	messagebox.showinfo(message=m_text, title = "Infos")
menuleiste = Menu(tkFenster)

exit_button = Button(tkFenster, text="Beenden", command=tkFenster.quit)

datei_menu = Menu(menuleiste, tearoff=0)
help_menu = Menu(menuleiste, tearoff=0)

datei_menu.add_command(label="Anwenden", command=button_action)
datei_menu.add_separator()
datei_menu.add_command(label="Exit", command=tkFenster.quit)

help_menu.add_command(label="Info!", command=action_get_info_dialog)

menuleiste.add_cascade(label="Datei", menu=datei_menu)
menuleiste.add_cascade(label="Help", menu=help_menu)

exit_button.place(x=150, y=250)

tkFenster.config(menu=menuleiste)  
# Aktivierung des Fensters
tkFenster.mainloop()