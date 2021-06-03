import tkinter as tk  
from functools import partial
from tkinter import messagebox
import time
from tkinter import *
   
   
def call_result(label_result, n1, n2):  
    num1 = (n1.get())  
    num2 = (n2.get())  
    result = int(num1)+int(num2)  
    label_result.config(text="Result = %d" % result)  
    return  
   
root = tk.Tk()  
root.geometry('300x400')  
  
root.title('Calculator addition')  
   
number1 = tk.StringVar()  
number2 = tk.StringVar()  
  
labelNum1 = tk.Label(root, text="Zahl 1").grid(row=2, column=0)  
  
labelNum2 = tk.Label(root, text="Zahl 2").grid(row=3, column=0)  
  
labelResult = tk.Label(root)  

labelResult.grid(row=8, column=2)  
  
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=2, column=2)  
  
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=3, column=2)  
  
call_result = partial(call_result, labelResult, number1, number2)  
  
buttonCal = tk.Button(root, text="Calculate", command=call_result).grid(row=4, column=2)  
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------

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