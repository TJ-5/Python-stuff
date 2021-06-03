import tkinter as tk  
from functools import partial
from tkinter import messagebox
import time
from tkinter import *
from tkinter import ttk
   
   

root = tk.Tk()  
root.geometry('300x400')  
  
root.title('Calculator addition')  

#Abfrage Männlich Weiblich

def callbackFunc(event):
     print("New Element Selected")

labelTop = tk.Label(root,
                    text = "Wähle dein Gender an")
labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(root, 
                            values=[
                                    "Männlich",
                                    "Weiblich"])


comboExample.grid(column=0, row=1)
comboExample.current(1)

comboExample.bind("<<ComboboxSelected>>", callbackFunc)
if(comboExample=="Männlich"):
    print("Test")

#Menüleite und Zeit

def Zähler(counter = 0):
    counter += 1
    Aktuell = time.ctime()
    DatumZeit.config(text=Aktuell)
    root.after (1000, Zähler, counter)

def Fenster_Inhalt():
    Aktuell = time.ctime()
    DatumZeit.config(text=Aktuell)


DatumZeit = Label(root, font=("Arial 10 bold"),
              width=1,
              height=1, bg="white",
              fg="black",
              text="OK")
DatumZeit.place(x=200, y=0, width=100, height=15)

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
menuleiste = Menu(root)

exit_button = Button(root, text="Beenden", command=root.quit)

datei_menu = Menu(menuleiste, tearoff=0)
help_menu = Menu(menuleiste, tearoff=0)

datei_menu.add_command(label="Anwenden", command=button_action)
datei_menu.add_separator()
datei_menu.add_command(label="Exit", command=root.quit)

help_menu.add_command(label="Info!", command=action_get_info_dialog)

menuleiste.add_cascade(label="Datei", menu=datei_menu)
menuleiste.add_cascade(label="Help", menu=help_menu)

exit_button.place(x=180, y=350)

root.config(menu=menuleiste)  
root.mainloop()